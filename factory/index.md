# Factory Mode

Depending on electrical conditions or ambiant temperature, your module CV and knobs might be slightly off and might require recalibration.
You might have also bought the Groove or Performer expanders, and calibration ensures that those expanders are running with optimal performance.

Also, should you have a problem with the module, our support team will ask you to run "test mode" to have a rough idea of what the problem is.

This operation requires a bit of care because the module will need to be powered by your Eurorack case in order to complete successfully. You will also need a simple LFO and VCO.
For test mode or when recalibrating the central Bohm module, a stable 3V voltage source is also required.

## Entering Test Mode and Calibration

To enter test mode and calibration:

1. **Turn off** your Eurorack system
1. **Remove all the Eurorack patch cables** connected to the module
1. Remove the module from the rack, but **keep its power cord attached**
1. Place the module on a **non-conductive surface**
1. **Press** the {guilabel}`FLASH_SW` button at the top, between the two printed circuit boards of the module, **keep it pressed**, and **turn on** your Eurorack system. The test mode welcome screen will appear
1. Press {guilabel}`FUNCTION`, the screen will turn entirely white. Check that the screen is working properly, and press {guilabel}`FUNCTION` again

The screen will show something similar to:
```
DETECTED
BOHM
GROOVE
PERFORMER
```

Make sure that all your expanders appear in that list. Then:

- To only calibrate the expanders, click the {guilabel}`FUNCTION` button
- To calibrate all modules or if test mode is required, press the {guilabel}`FUNCTION` button for at least 1 second

## Calibrating Expanders

If the Groove expander is present:

1. Check that the {guilabel}`CLOCK` LED is blinking, press {guilabel}`FUNCTION`
1. Turn the {guilabel}`2` knob fully on the left, then fully on the right, then press {guilabel}`FUNCTION`
1. Repeat the previous step for the {guilabel}`3`, {guilabel}`4`, {guilabel}`LENGTH`, {guilabel}`PITCH`, {guilabel}`FX`, {guilabel}`COLOR` knobs, {guilabel}`VOL` slider, and then for the {guilabel}`FX`, and {guilabel}`COLOR` attenuverter trims
1. Acknowledge that you have already removed all patch cables and press {guilabel}`FUNCTION`
1. Wait until the module calibrates CVs automatically
1. Use your LFO in sinus mode and connect it to the {guilabel}`FX` CV
1. Repeat the previous step for {guilabel}`CLOCK`, {guilabel}`COLOR`, {guilabel}`VOL`, {guilabel}`LENGTH`, {guilabel}`PITCH`, and {guilabel}`TAP` CVs
1. Connect a cable between the {guilabel}`TAPS` CV output and {guilabel}`TAPS` CV input, then press {guilabel}`FUNCTION`

If the Performer expander is present:

1. Press the {guilabel}`ON/OFF` button
1. Check that the {guilabel}`ON/OFF` LED is blinking, press {guilabel}`FUNCTION`
1. Turn the {guilabel}`DUCK` knob fully on the left, then fully on the right, then press {guilabel}`FUNCTION`
1. Repeat the previous step for the {guilabel}`FX` knobs and {guilabel}`VOL` slider
1. Acknowledge that you have already removed all patch cables and press {guilabel}`FUNCTION`
1. Wait until the module calibrates CVs automatically
1. Use your LFO in sinus mode and connect it to the {guilabel}`DUCK` CV
1. Repeat the previous step for {guilabel}`FX`, {guilabel}`ON/OFF` and {guilabel}`VOL` CVs
1. Use your VCO in sinus mode and **connect it to the right input {guilabel}`IN` first**
1. Repeat the previous step with the left input {guilabel}`IN`

After the expanders have been calibrated, `CALIBRATION SAVED` will appear
on the screen. Clicking the {guilabel}`FUNCTION` will show the "QC passed" stamp,
which means that your module is in specs (no problem were found) and calibration is complete.

You can now turn off your Eurorack system, and reinstall the module into your rack.

## Test Mode

The full test mode is only required if requested from our support team, or if
electrical conditions or ambiant temperature necessitated it.

It is completely similar to the expanders calibration, except the central
Bohm module will be also tested and calibrated. For this reason you will need,
on top of the LFO/VCO requirements for the expanders, a stable 3V voltage source.

Typically, you will want to use a Eurorack sequencer, or a MIDI to CV module.

If you are only testing the module and don't have a stable 3V voltage source, you can
turn off your Eurorack system before reaching the `CALIBRATION SAVED` step
mentioned in the previous section.

1. Press the {guilabel}`HIT` button
1. Check that the {guilabel}`HIT` LED is blinking, press {guilabel}`FUNCTION`
1. Make sure a SD card is in the microSD card slot and press {guilabel}`FUNCTION`
1. Read the SD card test status and press {guilabel}`FUNCTION`
1. Turn {guilabel}`FUNCTION` 10 times on the left, then 10 times on the right
1. Turn the {guilabel}`LENGTH` knob fully on the left, then fully on the right, then press {guilabel}`FUNCTION`
1. Repeat the previous step for the {guilabel}`SUSTAIN`, {guilabel}`ATTACK`, {guilabel}`PITCH`, {guilabel}`CURVE`, {guilabel}`TRS DECAY`, {guilabel}`COLOR`, {guilabel}`FX`, {guilabel}`TRS TONE` knobs, and then for the {guilabel}`LENGTH`, {guilabel}`SUSTAIN`, {guilabel}`PITCH` and {guilabel}`COLOR` attenuverter trims
1. Acknowledge that you have already removed all patch cables and press {guilabel}`FUNCTION`
1. Wait until the module calibrates CVs automatically
1. Use your LFO in sinus mode and connect it to the {guilabel}`LENGTH` CV
1. Repeat the previous step for {guilabel}`ATTACK`, {guilabel}`SUSTAIN`, {guilabel}`HIT`, {guilabel}`PITCH`, {guilabel}`CURVE`, {guilabel}`COLOR`, {guilabel}`TRS DECAY`, {guilabel}`TONE`, {guilabel}`FUNCTION`, {guilabel}`VELOCITY` and {guilabel}`FX` CVs
1. Connect a cable between your stable 3 Volts source and {guilabel}`PITCH` CV input, then press {guilabel}`FUNCTION`
1. Wait until the module calibrates the {guilabel}`PITCH` CV automatically
1. Connect a patch cable from {guilabel}`OUT` left to your audio output and make sure a 440Hz tone is playing, press {guilabel}`FUNCTION`
1. Repeat the previous step with {guilabel}`OUT` right

The test mode and calibration will then follow with the present expanders if any.
For more details, follow the instruction in the previous section.
