#!/usr/bin/env python3

"""POCKETROCKIT
"""

import importlib.metadata
import logging
import shutil
import sys
from argparse import ArgumentParser
from argparse import Namespace as Args
from collections.abc import Sequence
from contextlib import suppress
from pathlib import Path

from pocketrockit.commons import SfConfig
from pocketrockit.engine import load_module
from pocketrockit.misc import setup_logging


def parse_args(argv: Sequence[str] | None = None) -> Args:
    """Cool git like multi command argument parser"""
    parser = ArgumentParser(__doc__)
    parser.add_argument("--verbose", "-v", action="store_true")

    parser.set_defaults(func=lambda *_: parser.print_usage())
    subparsers = parser.add_subparsers(help="available commands", metavar="CMD")

    parser_info = subparsers.add_parser("help")
    parser_info.set_defaults(func=lambda *_: parser.print_help())

    parser_info = subparsers.add_parser("info")
    parser_info.set_defaults(func=fn_info)

    parser_play = subparsers.add_parser("play", aliases=["p", "run"])
    parser_play.set_defaults(func=fn_play)
    parser_play.add_argument("path", type=Path, default=".", nargs="?")

    parser_init = subparsers.add_parser("init")
    parser_init.set_defaults(func=fn_init)
    parser_init.add_argument("path", type=Path, default=".", nargs="?")

    parser_list_sf2 = subparsers.add_parser("list-sf2")
    parser_list_sf2.set_defaults(func=fn_list_sf2)
    parser_list_sf2.add_argument("path", type=Path, default=".")

    return parser.parse_args(argv)


def logger() -> logging.Logger:
    """Named logger"""
    return logging.getLogger("pr.cli")


def extract_version() -> str:
    """Returns either the version of installed package or the one
    found in nearby pyproject.toml"""
    with suppress(FileNotFoundError, StopIteration):
        with open(
            Path(__file__).parent.parent / "pyproject.toml", encoding="utf-8"
        ) as pyproject_toml:
            version = (
                next(line for line in pyproject_toml if line.startswith("version"))
                .split("=")[1]
                .strip("'\"\n ")
            )
            return f"{version}-dev"
    return importlib.metadata.version(__name__.split(".", maxsplit=1)[0])


__version__ = extract_version()


def shorten_home(path: Path | str) -> Path:
    """Reverse of expanduser"""
    return Path(Path(path).as_posix().replace(str(Path.home()), "~"))


def fn_info(_args: Args) -> None:
    """Entry point `info`"""
    print(f"Version: {__version__} (at {shorten_home(Path(__file__).parent)})")
    print(
        f"Python: {'.'.join(map(str, sys.version_info[:3]))}"
        f" (at {shorten_home(sys.executable)})"
    )
    # Show MIDI info
    # Show Info about SoundFonts
    # Show Info about local track files


def fn_list_sf2(args: Args) -> None:
    """Entry point `list-sf2`"""

    sf2 = SfConfig(args.path)
    print("Use these entries in your .toml file:")
    print("")
    print("[[pocketrockit.midi.sf_load]]")
    print(f'filepath = "{args.path}"')
    print("instruments = [")

    for preset in sf2.instruments:
        print(
            f'    {{short="", name="{preset.name}"'
            f", bank={preset.bank}, preset={preset.preset}}},"
        )
    print("]")


def fn_play(args: Args) -> None:
    """Entry point `play`/`run`"""
    setup_logging()
    logger().debug("Args: %s", {k: str(v) for k, v in args.__dict__.items()})
    load_module(args.path)


def fn_init(args: Args) -> None:
    """Entry point `init`"""
    template_target = args.path / "template.py"
    print(
        "\n".join(
            line.lstrip().split("|", 1)[-1]
            for line in """
            Make sure the following requirements are met:
            [ ] FluidSynth is installed and running
            [ ] SoundFont files `instrumental.sf2` and `drums.sf2` are present
            |   (see https://projects.om-office.de/frans/pocketrockit/-/blob/main/Readme.md)
            |   - test with `fluidsynth -i -a pipewire -z 256 -g 0.5 instrumental.sf2 <MIDI_FILE>`
            [ ] A pocketrockit track file is available
            """.split(
                "\n"
            )
        )
    )

    if template_target.exists():
        print(f"{template_target} already exists - won't be overwritten")
    else:
        shutil.copy(Path(__file__).parent / "examples" / "template.py", template_target)
        print(f"A file {template_target} has been made available - take it as a starting point!")


def main() -> int:
    """Entry point for everything else"""
    (args := parse_args()).func(args)
    return 0


if __name__ == "__main__":
    main()
