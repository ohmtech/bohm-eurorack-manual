# System Settings

The system settings are accessed by pressing the {guilabel}`FUNCTION` button
for at least 2 seconds.

## Post EQ option

This option allows to set an EQ on the signal output. The signal output EQ only affects Bohm and Groove, but not the Performer audio input.

The Post EQ has:
- 1 low shelf, with configurable frequency and level
- 1 peak filter, with configurable frequency, gain and Q factor
- 1 high shelf, with configurable frequency and level

By default, all levels and gains are set to 0dB, so the post EQ has no effect.

Note that the Post EQ is a system setting and not a per-model setting.
Its intent is to be able to make quick EQ changes before a live set in a club,
for example if the PA over-emphasizes bass frequencies.


## In Vol option

By default, the audio input volume on Performer is 0dB.
This option allows to lower the volume of the external audio input
from -60dB to 0dB, in 1dB steps.

It is a convenience feature to lower the volume of a module without output level
control directly connected to Bohm,
allowing to save one VCA in limited rack space configuration (live sets).


## Perf Vol option

By default, the {guilabel}`VOL` slider and CV on Performer controls the volume
of the combined Bohm and Groove, to balance it against the Performer external
audio input.
It is possible to select which signal is controlled by {guilabel}`VOL`:

- `B+G`: Bohm and Groove
- `BOHM`: Bohm only

This feature also allows to make the Groove drone without hearing the Bohm kick.


## Perf Max option

By default, when {guilabel}`VOL` slider or CV are to the max, the output of
the Bohm and/or Groove are at their maximum, 0dB.

It is possible to set the maximum level when the {guilabel}`VOL` slider or CV
are to the max, from -18dB to 0dB, in 1dB steps.

This allows to put back the Bohm volume to a desired level in live with a swift gesture,
without having to aim for a precise slider position.


## Pitch CV option

By default, the {guilabel}`PITCH` CV is not tracking musical pitch and the entire kick octave
can be CV controlled using for example a LFO with a ±5V output range.

Bohm can pitch track the kick octave using Volt/Octave. This options then allows
to select the 1V voltage range to map to the octave, either 0..1V, 1..2V or 2..3V.


## ATTVERT 2 option

By default, the {guilabel}`SUSTAIN` attenuverter is mapped to the {guilabel}`SUSTAIN` CV.
It is however possible to map it instead to the {guilabel}`VELOCITY` CV.


## Func Rand option

By default, the {guilabel}`FUNCTION` trigger in Studio mode will randomize only
the Bohm and Groove (_ie._ not the performer). It is possible to randomize
everything using this option:

- `ALL`: Randomize Bohm, Groove and Performer
- `B+G`: Randomize only Bohm and Groove


## Perf FX option

By default, activating or deactivating the Performer FX section is synced to
{guilabel}`HIT`. It is also possible to toggle it immediately:

- `INSTANT`: Toggle FX section immediately
- `SYNCED`: Sync FX to next {guilabel}`HIT`


## Perf ON/OFF option

By default, pressing the {guilabel}`ON/OFF` button or sending a trigger to
the {guilabel}`ON/OFF` CV will toggle the FX activation.
It is also possible to have a gate behavior:

- `TRIG`: Toggle FX on trigger or button click
- `GATE`: Activate FX while CV is on or button is hold


## Grv Env option

By default, the groove envelope will fall after the 4th tap. It is also possible to sustain it, to use Groove as a drone, or when there is more than 4 taps between two {guilabel}`HIT` (typically at higher tempos):

- `FALL`: Fall the envelope after the 4th tap
- `SUSTAIN`: Sustain the envelope at 4th tap level after the 4th tap

## Taps Out option

By default, the {guilabel}`TAPS` output CV emits the envelope of the Groove.
It is also possible to emit the Bohm or Performer envelopes:

- `GROOVE`: Groove envelope
- `I BOHM`: Inverted Bohm envelope
- `PERF`: Performer envelope


## Panning option

By default the stereo audio input signal, the Bohm signal and Groove signal are processed in stereo. This option allows to place those signals either on the audio output left or right channel. This makes possible to selectively process further those signals using other Eurorack modules, but in mono.

- `BOHM`: sets the main kick voice panning mode
- `GROOVE`: sets the secondary kick voice panning mode
- `PERFORMER`: sets the audio input panning mode

The panning modes are:
- `LEFT`: The stereo signal is hard-panned left, and will output on the audio output left channel only
- `CENTER`: The stereo signal remains untouched
- `RIGHT`: The stereo signal is hard-panned right, and will output on the audio output right channel only


## Scrn Saver option

By default, the screen saver option is `ON`, as it is important to maximize the
lifetime of your Bohm OLED screen. However in some situations it might
undesirable, for example when shooting a video or during a live
performance.
The screen saver can therefore be turned `OFF` to accomodate those cases.


## Lock Model option

When using the Bohm in live but using `STUDIO` mode instead of one of the live
modes, an accidental rotation of the {guilabel}`FUNCTION` encoder will change the model.

This option allows to lock the current selected model in `STUDIO` mode.

This setting is not persistent: when the Bohm is powered up
the {guilabel}`FUNCTION` encoder rotation is always unlocked.


## Shop Mode option

By default, the module will remember the last model used, as well as all variations
settings of the last 12 models used, and the other system settings listed above.

By turning on the Shop Mode option, one can prevent that, allowing a shop owner
to reset the module in the same condition for customers to have the same
initial experience with the module. 


## Backup/Restore

One can backup the entire internal memory of the Bohm into a file on the SD card. This backup contains everything, the module setup as well as all the programs and snapshots of the module.

Those backups can then be archived on a computer, and one can use them to manage multiple live performances.

- `BACKUP` will copy the entire internal memory to a `backup.bohm` file on the SD card. **If a file already exists with the same name on the SD card, it will be overwritten**
- `RESTORE` will copy a file found with extension `.bohm` on the SD card and copy it to the internal memory. A file can then be named for example `my_live_at_berghain_2025.bohm`, but you must ensure to have **only one `.bohm` file on the SD card**

While backup contains the module calibration, restoring restores everything except the module calibration.

Restoring takes a few seconds, and the module will automatically restart after it is completed.


## Factory Reset

One can reset the module back to the same state as when it left our factory. Resetting to factory settings will reset all the system settings listed above, as well as all the programs and snapshots. However it will keep the factory calibration data.

```{warning}
Factory reset will remove everything in the Bohm internal memory, including programs and snapshots. It is advised to backup the module before doing so.
```

Factory reset takes a few seconds, and the module will automatically restart after it is completed.
