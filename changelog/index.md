# Changelog

## Version 2026.0311.1445

- Performer FX LED shows now an intermediate state (blinking) while transitioning and waiting for {guilabel}`HIT` in synced mode
- New `PERF ON/OFF` system setting allows to either toggle FX (`TRIG`, old behavior, default) or set FX as a gate (`GATE`)
- New `LOCK MODEL` system setting to prevent accidental model changes in a live set when using `STUDIO` mode. It is automatically turned off when powering up Bohm
- New `TAPS OUT` system setting to select which envelope to output from Groove (`GROOVE`, old behavior, default), Inverted Bohm (`I BOHM`), Performer ducking (`PERF`) or (non-inverted) Bohm envelope (`BOHM`)
- New `IN VOL` system setting to lower the volume of the external audio input
- New `PERF VOL` system setting to select which signals are affected by the Performer volume slider/CV, either Bohm and Groove (`B+G`, old behavior, default) or only Bohm (`BOHM`)
- New `PERF MAX` system setting to restrict the maximum volume when slider or CV is full on
- New `DUCK TIME` model setting to change the release time of the ducking curve
- New `DUCK SMTH` model setting to smooth the ducking curve
- New `DUCK BS` model setting to set the maximum frequency below which the ducking is operating
- New `LAYER VOL` setting in the XT-88 model, to set the volume of the layering sample
- New `POST EQ` system settings as a sub-menu, with 1 low shelf, 1 peak filter (boost/cut) and 1 high shelf
- OLP4 model now supports Groove
- When using HIT in sustain mode (using a long gate), Bohm can now reach C1 and C2 for every position of `CURVE`
- It is now possible to load a snapshop with pots positions, which allows to copy a snapshot or make tweaks when preparing a live performance


## Version 2025.0827.1600

- New engine version with system settings variations allows a system setting to now "talk" to the model
- New `GRV ENV` system settings allows the Groove envelope to `FALL` after the 4th tap (new feature, now the default when at factory settings), or `SUSTAIN` (old behavior, drone)
- Shop mode now also reset base system settings to their default on start, to ensure a consistent customer experience in shops' showrooms
- Fixed a flaw where 1 second was needed (for rate limiting) for a program clear or snapshot saving to be effectively written to internal memory. This is now immediate
- New `FACTORY RESET` system menu, to put back Bohm at the same state as when it left the factory (ie. everything is reset apart from calibration)
- New `BACKUP` and `RESTORE` menus to backup and restore the entire Bohm system (apart from calibration) to/from a file on the SD card
- New end of chain soft clipper that prevents hard clipping when input signal is too strong. The soft clipper starts to slowly clip above 0dB (±5V in Eurorack), with the 4.6dB headroom the audio codec has
- `DJ FILTER` (`NEUTRAL`/`RAVE`) has been changed to `DJ RESO` to control the filter resonance from 0% to 100%, in 10% increments. The `RAVE` lowest frequency in the `LP` portion used to be limited to 500Hz, this is no longer the case
- New Stereo width variation for Groove and Bohm models, when the signal is not already mono
- New `PANNING` system settings, allows each signals (Bohm, Groove, Audio Input) to be either stereo (default), hard-panned left or hard-panned right 


## Version 2025.0722.1625

- Initial release
