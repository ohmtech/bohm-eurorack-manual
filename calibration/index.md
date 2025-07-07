# Calibration Mode

In the factory, your Bohm has been calibrated with Groove and Performer expanders,
but there are little chances that those are the same Groove or Performer you
purchased.
The calibration data already present in your Bohm might be already good enough,
but you might want to calibrate Groove and/or Performer to achieve optimal performance.

Furthermore, depending on electrical conditions or ambiant temperature,
your module CV and knobs might be slightly off and might require recalibration.

Configuring the Groove and Performer expanders doesn't require any special equipment.

Configuring the Bohm module requires an Eurorack-compatible device that can produce 3V
for {guilabel}`PITCH` CV calibration, typically a Volt/Octave device such
as the Arturia Beatstep Pro or the Intellijel µMIDI Eurorack module.

The video below shows how to calibrate the Groove and Performer expanders.
The entire operation takes a little bit more than 1 minute.

```{youtube} pTN_Q4WiiRo
:width: 100%
```

The rest of this chapter is a textual version of it.


## Entering Calibration Mode

To enter calibration mode:

1. **Turn off** your Eurorack system
1. **Remove all the Eurorack patch cables** connected to the module
1. **Press** the {guilabel}`FUNCTION` button, **keep it pressed**, and **turn on** your Eurorack system
1. A welcome message will appear, follow the onscreen instructions

After the welcome message, the screen will show something similar to:
```
DETECTED
BOHM
GROOVE
PERFORMER
```

Make sure that all your expanders appear in that list. Then:

- To only calibrate the Groove and/or Performer expanders, click the {guilabel}`FUNCTION` button
- To calibrate all modules, press the {guilabel}`FUNCTION` button for at least 1 second

## Calibrating Expanders

If the Groove expander is present:

1. Turn the {guilabel}`2` knob fully on the left, then fully on the right, then press {guilabel}`FUNCTION`
1. Repeat the previous step for the {guilabel}`3`, {guilabel}`4`, {guilabel}`LENGTH`, {guilabel}`PITCH`, {guilabel}`FX`, {guilabel}`COLOR` knobs, {guilabel}`VOL` slider, and then for the {guilabel}`FX`, and {guilabel}`COLOR` attenuverter trims
1. Acknowledge that you have already removed all patch cables and press {guilabel}`FUNCTION`
1. Wait until the module calibrates CVs automatically

If the Performer expander is present:

1. Turn the {guilabel}`DUCK` knob fully on the left, then fully on the right, then press {guilabel}`FUNCTION`
1. Repeat the previous step for the {guilabel}`FX` knobs and {guilabel}`VOL` slider
1. Acknowledge that you have already removed all patch cables and press {guilabel}`FUNCTION`
1. Wait until the module calibrates CVs automatically

After the expanders have been calibrated, `CALIBRATION SAVED` will appear
on the screen. Clicking the {guilabel}`FUNCTION` button will restart the module.


## Calibrating Bohm and Expanders

Calibrating Bohm is only required if you observed that your Bohm CV and knobs are slightly off.

Configuring the Bohm module requires an Eurorack-compatible device that can produce 3V
for {guilabel}`PITCH` CV calibration, typically a Volt/Octave device such
as the Arturia Beatstep Pro or the Intellijel µMIDI Eurorack module.

```{note}
If you suddenly realize mid-way that your 3V source is missing or not good enough,
don't be scared: nothing is written into the Bohm internal memory until the very last `CALIBRATION SAVED` step.
You can cancel the procedure at any time by turning your Eurorack system off.
```

1. Turn the {guilabel}`LENGTH` knob fully on the left, then fully on the right, then press {guilabel}`FUNCTION`
1. Repeat the previous step for the {guilabel}`SUSTAIN`, {guilabel}`ATTACK`, {guilabel}`PITCH`, {guilabel}`CURVE`, {guilabel}`TRS DECAY`, {guilabel}`COLOR`, {guilabel}`FX`, {guilabel}`TRS TONE` knobs, and then for the {guilabel}`LENGTH`, {guilabel}`SUSTAIN`, {guilabel}`PITCH` and {guilabel}`COLOR` attenuverter trims
1. Acknowledge that you have already removed all patch cables and press {guilabel}`FUNCTION`
1. Wait until the module calibrates CVs automatically
1. Connect a cable between your stable 3 Volts source and {guilabel}`PITCH` CV input
1. The module shows the voltage value measured, and it should be close to 3000mV. Adjust the voltage (typically the octave on your device) as necessary. When this is done, press {guilabel}`FUNCTION`
1. Wait until the module calibrates the {guilabel}`PITCH` CV automatically

The test mode and calibration will then follow with the available expanders if any.
For more details, follow the instructions in the previous section.
