#!/usr/bin/env python3

"""POCKETROCKIT engine
"""
# pylint: disable=too-many-locals
# pylint: disable=too-many-instance-attributes
# pylint: disable=fixme

import asyncio
import concurrent
import logging
import threading
import time
from asyncio import sleep as async_sleep
from collections.abc import (
    Generator,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    MutableSequence,
    Sequence,
)
from dataclasses import dataclass, field
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_file_location
from itertools import chain, count
from pathlib import Path
from signal import SIGINT, SIGTERM
from types import ModuleType

from asyncinotify import Inotify, Mask

from .commons import MidiEvent, PriConfig
from .midi_io import midi_input_device, midi_output_device
from .misc import Singleton, colored, error, keyboard_reader, setup_logging, watchdog

MidiCmd = tuple[int, int, None | int]
CmdTrace = tuple[int, int, int]
Command = tuple[CmdTrace, str, Sequence[MidiCmd]]
Player = Generator[Command, None | int, None]


EMPTY_COMMAND: Command = (-1, -1, -1), "", []


@dataclass
class Env:
    """Some global environment"""

    # number of ticks per line - a line has typically 4 beats,
    # and should be dividable a number of times without loss of precision,
    # so we combine a number of typical dividers
    step_size: int = 4 * 16 * 3 * 5  # 960
    bpm: int = 120


@dataclass
class Stage(metaclass=Singleton):
    """Access to the currently played music"""

    env: Env = field(default_factory=Env)
    active: bool = False
    # On startup we want the current track definition to be free from errors. Verified will
    # be set once we successfully read from all generators
    verified: bool = False
    players: Mapping[str, Player] = field(default_factory=dict)
    new_track: None | MutableMapping[str, Player] = None
    file_to_track: str = ""
    tick: int = -1
    pause: bool = False
    step: bool = False
    mod: int = 0
    modifiers: MutableSequence[object] = field(default_factory=list)


def load_module(filepath: str | Path) -> ModuleType:
    """(Re)loads a python module specified by @filepath"""
    logger().debug("load module '%s' from '%s'", Path(filepath).stem, filepath)
    spec = spec_from_file_location(Path(filepath).stem, filepath)
    if not (spec and spec.loader):
        raise RuntimeError("Could not load")
    module = module_from_spec(spec)
    assert module
    assert isinstance(spec.loader, SourceFileLoader)
    loader: SourceFileLoader = spec.loader
    # here the actual track definition takes place
    loader.exec_module(module)
    return module


def note_generator() -> Iterator[Iterable[MidiCmd]]:
    """Brings all players together and cleans up played notes"""
    active_notes: MutableMapping[tuple[int, int], int] = {}
    stage = Stage()

    for tick in count():
        stage.tick = tick

        if tick % stage.env.step_size == 0:
            logger().debug(
                "== tick: %d, step: %d, step_size: %d ==",
                tick,
                tick / stage.env.step_size,
                stage.env.step_size,
            )

        all_commands: MutableSequence[MidiCmd] = []
        for name, stream in stage.players.items():
            try:
                source_pos, origin, commands = next(stream)
                if commands:
                    logger().debug("%s: %s:%s => %s", name, source_pos, origin, commands)
                if commands:
                    all_commands.extend([(a, b + stage.mod, c) for a, b, c in commands])
            except StopIteration:
                pass
            except Exception as exc:  # pylint: disable=broad-except
                if not stage.verified:
                    raise
                error(f"exception in play: {exc}")

        stoppers = []
        for (active_channel, active_note), store_tick in list(active_notes.items()):
            # send noteoff for any still played note
            if tick - store_tick > stage.env.step_size // 4:
                stoppers.append((active_channel, active_note, None))
                del active_notes[active_channel, active_note]
        for channel, note, _velocity in all_commands or []:
            # print((channel, note), active)
            if (channel, note) in active_notes:
                # send noteoff for next note to be played
                stoppers.append((channel, note, None))
                del active_notes[channel, note]

            active_notes[channel, note] = tick

        # print(tick, active_notes)
        yield chain(stoppers, all_commands)


@watchdog
async def music_loop() -> None:
    """Main loop collecting instructions to send it to MIDI"""
    stage = Stage()

    config = PriConfig("pocketrockit.toml")

    with midi_output_device(config.midi) as midi_out:
        for i in count():
            # Wait for players to emerge the first time (otherwise `tick` won't start at 0).
            # Inform the user, if there is nothing there yet.
            if stage.players:
                break
            if i % 10 == 0:
                logger().info("no `players` defined yet..")
            await async_sleep(0.1)

        # time progressor - for drift-less looping
        time_ladder = time.time()

        for notes in note_generator():
            for channel, note, velocity in notes:
                try:
                    if velocity is None:
                        # print("OF", (channel, note))
                        midi_out.noteoff(channel, note)
                    else:
                        stage.step = False
                        # print("ON", (channel, note, velocity))
                        midi_out.noteon(channel, note, velocity)
                except Exception as exc:  # pylint: disable=broad-except
                    error(f"Unhandled exception in MIDI playback: {exc}")
            while True:
                # make me absolute please

                # A BPM of 60 typically means we have a duration of 1sec per quater note.
                # A typical 4/4 line would then take 4sec. Env.step_size is the number of ticks
                # per line, so a step_size of 48 would lead to a duration per tick of
                # 4 / 48 sec
                time_ladder += 60 / stage.env.bpm * 4 / stage.env.step_size
                await async_sleep(max(0, time_ladder - time.time()))

                if not stage.pause or stage.step:
                    break


@watchdog
async def watch_changes() -> None:
    """Watches for file changes in track definition file and reload on change"""
    stage = Stage()
    load_module(stage.file_to_track)
    with Inotify() as inotify:
        inotify.add_watch(
            Path(stage.file_to_track).parent,
            mask=Mask.CLOSE_WRITE | Mask.MOVED_TO | Mask.CREATE,
        )
        async for event in inotify:
            # Fixme - currently CLOSE_WRITE might happen twice - looks like we need a
            #         timer mechanism here
            # Fixme - we listen for all files now, regardless whether or not we need it
            #         is that a problem?
            assert event.path
            if not event.path.is_file() or event.path.stem.startswith("."):
                continue
            logger().debug("\033[0;33mpath: %s, mask: %r", event.path, event.mask)
            try:
                load_module(stage.file_to_track)
            except Exception as exc:  # pylint: disable=broad-except
                error(f"Unhandled exception in watch_changes: {exc}")


def logger() -> logging.Logger:
    """Named logger"""
    return logging.getLogger("pr.engine")


@watchdog
async def handle_keyboard(loop: asyncio.BaseEventLoop, terminator: threading.Event) -> None:
    """Handles key press event"""
    ticks = []
    try:
        async for key in keyboard_reader(loop, terminator):
            if key == " ":
                logger().info(colored("SPACE", "yellow"))
                Stage().pause = not Stage().pause
            elif key == ".":
                logger().info(colored("STEP", "yellow"))
                Stage().pause = True
                Stage().step = True
            elif key == "t":
                ticks.append(Stage().tick)
                logger().info(colored(f"{ticks}", "yellow"))
            else:
                logger().info(colored(key, "yellow"))
        logger().info("Keyboard loop stopped - terminate program")
        terminate(terminator)
    except RuntimeError as exc:
        logger().warning("Could not run keyboard handler: %s", exc)


@watchdog
async def handle_midi_input(loop: asyncio.BaseEventLoop, terminator: threading.Event) -> None:
    """Handles key press event"""
    event_queue: asyncio.Queue[MidiEvent] = asyncio.Queue()
    stage = Stage()
    with concurrent.futures.ThreadPoolExecutor() as pool:

        loop.run_in_executor(
            pool,
            midi_input_device,
            "pygame",
            ["OP-1", "Sylphyo", "USB MIDI Interface", "Midi Through"],
            loop,
            event_queue,
            terminator,
        )

        while True:
            event = await event_queue.get()
            if event.status == 176:
                logger().info("MIDI CTRL    %d => %d", event.data1, event.data2)
                if event.data1 == 1:
                    if event.data2 in {1, 127}:
                        stage.mod += -1 if event.data2 == 127 else 1
            elif event.status == 144:
                logger().info("MIDI NOTEON  %d => %d", event.data1, event.data2)
            elif event.status == 128:
                logger().info("MIDI NOTEOFF %d => %d", event.data1, event.data2)
            else:
                logger().warning("MIDI unknown %s", event)


def terminate(terminator: threading.Event) -> None:
    """Sends a signal to async tasks to tell them to stop"""
    try:
        terminator.set()
        for task in asyncio.all_tasks():
            task.cancel()
        asyncio.get_event_loop().stop()
    except Exception as exc:  # pylint: disable=broad-except
        logger().error("terminator got: %r", exc)


def run() -> None:
    """Runs the pocketrockit event loop forever"""
    setup_logging()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    terminator = threading.Event()

    # https://stackoverflow.com/a/71956673
    _tasks = {
        asyncio.ensure_future(handle_midi_input(loop, terminator)),
        asyncio.ensure_future(handle_keyboard(loop, terminator)),
        asyncio.ensure_future(music_loop()),
        asyncio.ensure_future(watch_changes()),
    }

    try:
        for signal_enum in [SIGINT, SIGTERM]:
            loop.add_signal_handler(signal_enum, lambda: terminate(terminator))
        loop.run_forever()
    finally:
        logger().debug("finally - loop.run_forever()")
