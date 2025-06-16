# Overview

Bohm comes preloaded with "models" which represents different kick drum machines
and their unique circuitry.

Each model has its own interpretation of the knobs positions. The following
section describes what concepts the models tend to follow in practice.

## Bohm

```{image} outline-bohm.svg
:width: 50%
:align: center
```

- {guilabel}`HIT`: Kick trigger
- {guilabel}`VELOCITY`: Kick velocity
- {guilabel}`LENGTH`: Kick duration
- {guilabel}`SUSTAIN`: Kick volume
- {guilabel}`ATTACK`: Kick attack amount
- {guilabel}`PITCH`: Pitch of the kick, from C1 (32.70Hz) to C2 (65.41Hz)
- {guilabel}`CURVE`: Pitch curve, from 808-style curve counterclockwise to 909-style curve clockwise
- {guilabel}`TRS DECAY`: Transient (click) duration
- {guilabel}`COLOR`: Timbre of the sub-bass oscillator
- {guilabel}`FX`: Amount of kick post-effect
- {guilabel}`TRS TONE`: Transient (click) tone, from dark counterclockwise to bright clockwise
- {guilabel}`FUNCTION`: Model and model variations selector
- {guilabel}`MICRO SD`: microSD slot for models, firmware and user-customisable wavetables and samples
- {guilabel}`OUT`: Stereo audio output

## Groove

```{image} outline-groove.svg
:width: 27.8%
:align: center
```

Groove is a secondary kick voice, typically used for techno rumbles or kick tops.

- {guilabel}`CLOCK`: Groove trigger
- {guilabel}`TAPS` ({guilabel}`2` {guilabel}`3` {guilabel}`4`) : Groove volume envelope
- {guilabel}`LENGTH`: Groove duration, relative to the Bohm kick duration
- {guilabel}`PITCH`: Groove pitch, relative to the Bohm kick pitch
- {guilabel}`COLOR`: Groove sound source
- {guilabel}`FX`: Amount of Groove post-effect
- {guilabel}`VOL`: Groove volume

## Performer

```{image} outline-performer.svg
:width: 22.2%
:align: center
```

- {guilabel}`IN`: Stereo audio input
- {guilabel}`DUCK`: Input ducking amount
- {guilabel}`FX`: Amount of performance effect
- {guilabel}`ON/OFF`: Performance effect activation toggle
- {guilabel}`VOL`: Volume of Bohm kick and Groove


