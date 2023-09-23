# ovos-launcher

Who is this repo for?

If these questions are something you can picture yourself asking, you are in the right place!
- where is the desktop icon?
- how do i install the app?
- I NEED start-mycroft.sh
- where do i click to run the assistant application
- what is the launch command
- what is a system daemon? what is systemd?
- I install ovos-core but nothing happpens, now what?

Hello newcomer! OpenVoiceOS provides a larger number of applications and packages, it is a Voice Operating System!
This can be overwhelming when you just want to try out and have a quick chat with a voice assistant, this repo tries to soften your introduction to ovos by providing the most accessible way to run the basic voice assistant stack

If you are a hardcore linux grey beard you probably are in the wrong place, you want each service as a [system daemon](https://github.com/OpenVoiceOS/ovos-systemd), you MUST have performance, you want to tune your config files, you want [native integration](https://github.com/OpenVoiceOS/raspbian-ovos/blob/dev/manual_user_install.sh) with your already existing OS! get out of this repo nerd!

## Install

install system libraries

debian: `sudo apt-get install -y build-essential python3-dev python3-pip python3-venv swig libssl-dev libfann-dev portaudio19-dev libpulse-dev cmake libncurses-dev pulseaudio-utils pulseaudio`

install ovos

`pip install ovos-launcher`

that's it!

#### Troubleshooting

if setup fails to install tflite_runtime in your platform, you can find wheels here https://whl.smartgic.io/ , install `tflite_runtime` first and then retry to install `ovos-launcher`

eg, for pyhon 3.11 in x86

`pip install https://whl.smartgic.io/tflite_runtime-2.13.0-cp311-cp311-linux_x86_64.whl`

## Running OVOS

by default you can only run OVOS 1 time, do not launch ovos multiple times! If you already have OVOS running as a system daemon, you are a nerd! wrong repo!

in the cli type `ovos-launcher`, that's it!

the essential OVOS stack is running in a single process with each service in it's own thread

```bash
$ovos-launcher --help

Usage: ovos-launcher [OPTIONS]

Options:
  -l, --listener TEXT  Choose a listener for mic input handling,
                       dinkum/old/classic
  --help               Show this message and exit.
```