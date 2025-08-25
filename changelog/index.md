# Changelog

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
