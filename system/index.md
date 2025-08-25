# System Settings

The system settings are accessed by pressing the {guilabel}`FUNCTION` button
for at least 2 seconds.

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


## Grv Env option

By default, the groove envelope will fall after the 4th tap. It is also possible to sustain it, to use Groove as a drone, or when there is more than 4 taps between two {guilabel}`HIT` (typically at higher tempos):

- `FALL`: Fall the envelope after the 4th tap
- `SUSTAIN`: Sustain the envelope at 4th tap level after the 4th tap


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
Factory reset will remove everything in the Bohm internaly memory, including programs and snapshots. It is advised to backup the module before doing so.
```

Factory reset takes a few seconds, and the module will automatically restart after it is completed.
