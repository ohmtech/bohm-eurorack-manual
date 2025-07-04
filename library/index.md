# Core Models Library

```{image} fm-2x.png
:width: 20%
:align: right
```
## FM-2X

The FM-2X model is a 2-operator carrier/modulator FM kick.
The carrier is a sub-bass oscillator
with frequency controlled by {guilabel}`PITCH` and its {guilabel}`CURVE`,
and amplitude controlled by {guilabel}`ATTACK`, {guilabel}`SUSTAIN`, {guilabel}`LENGTH` and {guilabel}`VELOCITY`
as described in the {doc}`/functions/index` chapter.

The carrier operator itself is a wavetable oscillator, and {guilabel}`COLOR`
controls the wavetable position:
- To a square waveform in the counterclockwise position,
- To a sinus waveform in the center position,
- To a triangle waveform in the clockwise position,

And waveforms interpolation in-between.

The modulator operator modulates the frequency of the carrier to bring the transient
typical of FM-based bass kicks.
{guilabel}`ATTACK` will control the frequency modulation amount of the first
operator to the second, while {guilabel}`TRS DECAY` controls the duration
at which the frequency modulation will decay, from 10ms to 100ms.

The modulator operator is itself as well a wavetable oscillator, and {guilabel}`TRS TONE`
controls the wavetable position, from counterclockwise to clockwise:
- Square,
- Derived Square,
- Quarter Sinus,
- Sinus,
- Half Sinus,
- Alternating Sinus,
- "Camel" Sinus,
- Positive Sinus,

And waveforms interpolation in-between.
Those waveforms are similar to the
[OPL3 waveforms](https://en.wikipedia.org/wiki/Yamaha_OPL#OPL3).

The ratio between the carrier frequency and the modulator frequency
can be adjusted in the model variations menus using the `RATIO` menu.
The possible ratio values are 0.5, 1 to 10, 12 and 15.

Another instance of those two operators is used for the Repetition sound source
of the Groove expander.


```{image} hz-1.png
:width: 20%
:align: right
```
## HZ-1

The HZ-1 model is a wavetable oscillator kick combined with a transient synthesizer.

The wavetable oscillator is frequency-controlled by {guilabel}`PITCH` and its {guilabel}`CURVE`,
and amplitude-controlled by {guilabel}`ATTACK`, {guilabel}`SUSTAIN`, {guilabel}`LENGTH` and {guilabel}`VELOCITY`
as described in the {doc}`/functions/index` chapter.

The {guilabel}`COLOR` parameter controls the amount and duration
of high frequency transients produced, by varying the wavetable position:
- Fully counterclockwise, the wavetable oscillator is just a sinus
- As the knob is turned clockwise, the oscillator sounds more distorted in the transient phase of the kick, but the tail remains a sinus
- Fully clockwise, the wavetable oscillator only reaches the sinus position if the {guilabel}`LENGTH` is long enough

The wavetable waveform itself can be changed using the `WT` model variation menu,
which a choice of "analog-style" waveforms.

The transient synthesizer type of click can be configured using the `CLK`
model variation menu, with a choice of different clicks, pops, ticks, and tocs.

Another instance of the wavetable oscillator is used for the Repetition sound
source, but without the transient synthesizer.


```{image} olp4.png
:width: 20%
:align: right
```
## OLP4

The OLP4 model is a 4-operator FM kick, insipired by the
[OPL3 chip](https://en.wikipedia.org/wiki/Yamaha_OPL#OPL3).
It is probably the most experimental model of the library.

The 4 operators are themselves as many wavetable oscillators, using the same
waveforms as described upper in the FM-2X model.
This time however, those waveforms are not interpolated and can be selected
using the `WF1` and `WF2` model varations menus:
- `WF1` selects the waveform for operator 1 and 3,
- `WF1` selects the waveform for operator 2 and 4.

The operators can be arranged in different configurations called "algorithms":
- `12`: operator 1 into operator 2, then to out,
- `1//2`, operator 1 and 2 in parallel, summed to out,
- `1234`, operator 1 to operator 4 in serie, then to out,
- `12//34`, operator into operator 2, in parallel of operator 3 into operator 4, summed to out,
- `1//234`, operator 1 in parallel of operator 2 to operator 4 in serie, summed to out,
- `1//23//4`, operator 1 in parallel of operator 2 into operator 3 and operator 4, summed to out.

```{image} olp4-algos.svg
:width: 100%
:align: center
```

{guilabel}`TRS TONE` controls the amount of FM feedback from operator 3 to
operator 1, which makes it more noisy. {guilabel}`COLOR` is inactive.

The Groove expander is not supported with this model.


```{image} pm-k1.png
:width: 20%
:align: right
```
## PM-K1

The PM-K1 model is a physical model of an acoustic bass drum.

This model is completely different from the others, and as such, all the
parameters have a different meaning:

- {guilabel}`PITCH` controls the size and tension of the bass drum,

- {guilabel}`ATTACK` controls the volume of the beater, typically captured at
   the microphone dedicated hole,
- {guilabel}`TRS TONE` controls the decay of the reverberation of the beater,
  leading to a more dark or brigther tone,

- {guilabel}`SUSTAIN` controls the volume of the ambiant microphone,
  and {guilabel}`LENGTH` the size of the room,

- {guilabel}`FX` controls the stereo spread of the ambiant microphone, from
  mono counterclockwise to wide clockwise.

All the other controls are inactive.

The Groove expander is not supported with this model.


```{image} px3.png
:width: 20%
:align: right
```
## PX3

The PX3 model is a wavetable oscillator kick with weird wavetables combined
with drum layering samples made of various objects hitting
diverse surfaces, post-processed with reverbs and distortions.
It tends to sound "harder" and "more experimental" than most other models.

The wavetable oscillator is frequency-controlled by {guilabel}`PITCH` and its {guilabel}`CURVE`,
and amplitude-controlled by {guilabel}`ATTACK`, {guilabel}`SUSTAIN`, {guilabel}`LENGTH` and {guilabel}`VELOCITY`
as described in the {doc}`/functions/index` chapter.

The {guilabel}`COLOR` parameter controls a function which modulates the wavetable position.

The wavetable waveform itself can be changed using the `WT` model variation menu.

Drum layering samples can be changed using the `LAYER` model variation menu.

Another instance of the wavetable oscillator is used for the Repetition sound
source, but without the drum layering sampler.


```{image} sp-6.png
:width: 20%
:align: right
```
## SP-6

The SP-6 model is a wavetable oscillator kick with "digital-sounding" wavetables combined
with drum layering samples made from synthesized transients (FM hihats and FM snares).

The wavetable oscillator is frequency-controlled by {guilabel}`PITCH` and its {guilabel}`CURVE`,
and amplitude-controlled by {guilabel}`ATTACK`, {guilabel}`SUSTAIN`, {guilabel}`LENGTH` and {guilabel}`VELOCITY`
as described in the {doc}`/functions/index` chapter.

The {guilabel}`COLOR` parameter controls the amount and duration
of high frequency transients produced, by varying the wavetable position:
- Fully counterclockwise, the wavetable oscillator is just a sinus
- As the knob is turned clockwise, the oscillator sounds more distorted in the transient phase of the kick, but the tail remains a sinus
- Fully clockwise, the wavetable oscillator only reaches the sinus position if the {guilabel}`LENGTH` is long enough

The wavetable waveform itself can be changed using the `WT` model variation menu.

Drum layering samples can be changed using the `LAYER` model variation menu.

Another instance of the wavetable oscillator is used for the Repetition sound
source, but without the drum layering sampler.


```{image} vx-t.png
:width: 20%
:align: right
```
## VX-T

The VX-T model is a wavetable oscillator kick combined with a transient synthesizer.

The wavetable oscillator is frequency-controlled by {guilabel}`PITCH` and its {guilabel}`CURVE`,
and amplitude-controlled by {guilabel}`ATTACK`, {guilabel}`SUSTAIN`, {guilabel}`LENGTH` and {guilabel}`VELOCITY`
as described in the {doc}`/functions/index` chapter.

The {guilabel}`COLOR` parameter controls the amount and duration
of high frequency transients produced, by varying the wavetable position:
- Fully counterclockwise, the wavetable oscillator is just a sinus
- As the knob is turned clockwise, the oscillator sounds more distorted in the transient phase of the kick, but the tail remains a sinus
- Fully clockwise, the wavetable oscillator only reaches the sinus position if the {guilabel}`LENGTH` is long enough

The wavetable waveform itself can be changed using the `WT` model variation menu,
which a choice of "analog-style" waveforms.

The transient synthesizer is a 4-operator FM based configuration,
where {guilabel}`TRS DECAY`
controls the amplitude decay, effectively leading in "toc" sounds counterclockwise
and hihat sounds clockwise. The synthesizer is then fed to a band-pass filter
for which {guilabel}`TRS TONE` controls the center frequency.

Another instance of the wavetable oscillator is used for the Repetition sound
source, but without the transient synthesizer.


```{image} wt-4.png
:width: 20%
:align: right
```
## WT-4

The WT-4 model is a wavetable oscillator kick with "analog-sounding" wavetables combined
with drum layering samples made from synthesized transients (FM hihats and FM snares).

The wavetable oscillator is frequency-controlled by {guilabel}`PITCH` and its {guilabel}`CURVE`,
and amplitude-controlled by {guilabel}`ATTACK`, {guilabel}`SUSTAIN`, {guilabel}`LENGTH` and {guilabel}`VELOCITY`
as described in the {doc}`/functions/index` chapter.

The {guilabel}`COLOR` parameter controls the amount and duration
of high frequency transients produced, by varying the wavetable position:
- Fully counterclockwise, the wavetable oscillator is just a sinus
- As the knob is turned clockwise, the oscillator sounds more distorted in the transient phase of the kick, but the tail remains a sinus
- Fully clockwise, the wavetable oscillator only reaches the sinus position if the {guilabel}`LENGTH` is long enough

The wavetable waveform itself can be changed using the `WT` model variation menu.

Drum layering samples can be changed using the `LAYER` model variation menu.

Another instance of the wavetable oscillator is used for the Repetition sound
source, but without the drum layering sampler.


```{image} xt-88.png
:width: 20%
:align: right
```
## XT-88

The XT-88 model is a wavetable oscillator kick combined
with drum layering samples, where the user can load their own wavetables
and samples.

There are 2 folders on the sd card, `wavetables` and `samples`. The user
can place their files in the corresponding folder. Only the WAVE file format
is supported.

The wavetables must be in the following format:
- Either generated from Xfer Records Serum or Serum 2, and a 2048 cycle length is assumed,
- Or Mono, 32-bit float, and a 1024 cycle length is assumed.

Additionally, a maximum of 16 wavetables can be loaded, or until the wavetable
1.4 Mbytes dedicated memory is full.

The samples must be in the following format:
- Mono or stereo
- 16-bit, 24-bit integer or 32-bit float
- 48kHz

Additionally, a maximum of 256 samples can be loaded, or until the sample
14 Mbytes dedicated memory is full.

The wavetable oscillator is frequency-controlled by {guilabel}`PITCH` and its {guilabel}`CURVE`,
and amplitude-controlled by {guilabel}`ATTACK`, {guilabel}`SUSTAIN`, {guilabel}`LENGTH` and {guilabel}`VELOCITY`
as described in the {doc}`/functions/index` chapter.

The wavetable waveform itself can be changed using the `WT` model variation menu,
and will display the loaded wavetables of the user.

{guilabel}`COLOR` controls the wavetable position. Then a modulated
EQ filter is applied to the output of the wavetable oscillator,
which brightness can be tuned using the `BRIGHT` model variation menu.

Drum layering samples can be changed using the `LAYER` model variation menu,
and will display the loaded samples of the user.

Another instance of the wavetable oscillator is used for the Repetition sound
source, but without the drum layering sampler.
