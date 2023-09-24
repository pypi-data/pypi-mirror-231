# POCKETROCKIT - A rocket in your pocket that rocks!

Original project page: https://projects.om-office.de/frans/pocketrockit.git

Write a music track in Python and play it while you write it (as you might know it from
[Sonic Pi](https://sonic-pi.net/), but written in Python (`sonic.py` was not available on PyPi, though)).

Write melodies, create rythm patterns, define endless simultaneously playing instruments, all in
a .. well .. simple Python syntax.


## Installation

```sh
[<PYTHON> -m] pip[3] install [--upgrade] pocketrockit
```


## Usage

Workflow is not quite mature yet, so here is the short version for now.

Create and enter a separate folder and provide required SoundFont files (configurable later,
hard-coded for now).

Pocketrockt expects two SoundFont files: `instrumental.sf2` and `drums.sf2`. You can download and
move/rename any file that works for you, and you can also just create symlinks (this is what I do).

This is just an example:

```sh
mkdir mytracks
cd mytracks
ln -s /usr/share/soundfonts/FluidR3_GM.sf2 instrumental.sf2
wget https://musical-artifacts.com/artifacts/2744/JV_1080_Drums.sf2
ln -s JV_1080_Drums.sf2 drums.sf2
```
The file `FluidR3_GM.sf2` was shipped with FluidSynth for me, and I got `JV_1080_Drums.sf2` from
[here](https://musical-artifacts.com/artifacts/2744).


Create a file `myfirsttrack.py` with the following content:

```python
#!/usr/bin/env python3

from pocketrockit import Env, midiseq, player, track

@track
def my_first_track(env: Env):

    @player
    def metronome():
        yield from midiseq("x x x x", channel=128, note=37)

    @player
    def melody1():
        yield from midiseq(
            "| .                .                 .                (II I)      "
            "| (II  VI<)        (IV< VI< . II<)   .                (II I)      "
            "| (II  VI<)        (IV< VI< . II<)   .                (II III)    "
            "| (IV  . III IV)   (. IV . II)       (III . II III)   (. III . I) "
            ,
            key="A5", channel=13)
```

Now - keeping the editor open for later use - execute this file. You can either make it executable
and run it directly or you run `python3` instead:

```sh
chmod +x myfirsttrack.py
./myfirsttrack.py

# or

python3 myfirsttrack.py
```


## Development & Contribution

```sh
pip3 install -U poetry pre-commit
git clone --recurse-submodules https://projects.om-office.de/frans/pocketrockit.git
cd pocketrockit
pre-commit install
# if you need a specific version of Python inside your dev environment
poetry env use ~/.pyenv/versions/3.10.4/bin/python3
poetry install
```

After modifications, this way a newly built wheel can be checked and installed:

```sh
poetry build
poetry run twine check dist/pocketrockit-0.0.25-py3-none-any.whl
python3 -m pip install --user --upgrade dist/pocketrockit-0.0.25-py3-none-any.whl
```


## Stuff to read / Sources

### SoundFonts

* https://musescore.org/en/handbook/3/soundfonts-and-sfz-files
* https://www.producersbuzz.com/category/downloads/download-free-soundfonts-sf2/
* https://archive.org/details/500-soundfonts-full-gm-sets
* https://ia802502.us.archive.org/view_archive.php?archive=/27/items/500-soundfonts-full-gm-sets/500_Soundfonts_Full_GM_Sets.zip
* https://musical-artifacts.com/artifacts?formats=sf2&tags=soundfont

flatpak install flathub com.polyphone_soundfonts.polyphone
flatpak run com.polyphone_soundfonts.polyphone instrumental.sf2


### Music stuff

* https://pianoscales.org/major.html
* https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
* https://onlinesequencer.net/181312
* https://github.com/Rainbow-Dreamer
* https://github.com/Rainbow-Dreamer/musicpy-daw
* https://sound.stackexchange.com/
* [librosa](https://librosa.org/doc/latest/advanced.html)
* [PO-20 Arcade key signatures for chords](https://pocketoperations.com/pocket-operator-cheatsheets.html#po-20-arcade-key-signatures-for-chords)

#### Drum patterns

* [Pocket Operations](https://shittyrecording.studio/)
* [10 Popular Drum Patterns Every Producer Should Know](https://www.youtube.com/watch?v=c7ffMObdxro)
* [Making Reggae & Dub music (2) Stepper beat](https://www.youtube.com/watch?v=o-qHwO8wE0c)
* [Dub Reggae Drum Beat Backing Track 150 bpm](https://www.youtube.com/watch?v=RCKn3TReYKM)
* [The Basics Of Reggae Drumming](https://www.youtube.com/watch?v=mxUHE5XC_mI)


### Tech stuff

* https://stackoverflow.com/questions/20023545/running-pyfluidsynth-pyaudio-demo-many-problems-with-alsa-and-jack
* https://www.ladspa.org/
* [How can I record audio output from command line in Linux?](https://superuser.com/questions/1570333/how-can-i-record-audio-output-from-command-line-in-linux)
* [Communicating between SuperCollider and Python](https://capital-g.github.io/musikinformatik-sose2021/00_basics/osc_communication.html)
* https://pypi.org/project/sc3/ / https://github.com/smrg-lm/sc3
* https://pypi.org/project/supercollider/ https://github.com/ideoforms/python-supercollider
* [supriya](https://github.com/josiah-wolf-oberholtzer/supriya)
* [TOML](https://toml.io/en/)


## Notation

* https://sneslab.net/wiki/Music_Macro_Language
* https://objectcomputing.com/resources/publications/sett/january-2008-writing-music-in-java-two-approaches
* https://mascii.org/
* https://www.mobilefish.com/tutorials/rtttl/rtttl_quickguide_specification.html
* https://pypi.org/project/musicpy/
* [Kodou](https://kodou.readthedocs.io/en/latest/)


## Similar projects

* https://foxdot.org/ / https://github.com/Qirky/FoxDot


## Troubles

* https://stackoverflow.com/questions/47247814/pygame-midi-init-function-errors

* Missing `/usr/local/share/alsa/alsa.conf`
```
ALSA lib conf.c:4555:(snd_config_update_r) Cannot access file /usr/local/share/alsa/alsa.conf
ALSA lib seq.c:935:(snd_seq_open_noupdate) Unknown SEQ default
```

```
sudo mkdir /usr/local/share/alsa
sudo ln -s /usr/share/alsa/alsa.conf /usr/local/share/alsa/alsa.conf
```
