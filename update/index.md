# Firmware Update

The firmware and models of your module can be conveniently updated using the provided
SD card.

Upgrading the firmware and models bring new features and bug corrections.
Current version is `2026.1023.0830`.

```{note}
[Register now](https://docs.google.com/forms/d/e/1FAIpQLSejDS4-5lSJu10RVo3Le0XZwoGzKYfNF74uzbf128DU1iingQ/viewform) to get early access to firmware updates and new models.
```

To check your firmware version, press the {guilabel}`FUNCTION` encoder for 2 seconds, turn the encoder to the right to navigate to the `ABOUT` menu, click the {guilabel}`FUNCTION` button, and look at the version displayed on the screen.

The latest SD card content, with firmware and latest models, is available
[here](https://s3.amazonaws.com/static.ohmforce.com/firmwares/bohm-eurorack-78de2ba1c91e59faf90c38d665a3388b33719283.zip).

To update the firmware and models, please follow the instructions below:

1. Download the zip archive above
2. Decompact the zip archive
3. Turn off your Eurorack system
4. Take the Bohm SD card out of the Bohm module
5. Insert the SD card in your computer-integrated or external SD card reader
6. Copy the content of the archive to the root of the SD card.
   For example, the file `Bohm.bin` **must** be at the top level of the SD card
7. Eject the card securely
8. Put back the Bohm SD card in the Bohm module
9. Turn on your Eurorack system

It will take around 20 seconds for the firmware to update, and nothing will
appear on the Bohm screen during that update.

The next time you will turn on your Eurorack system, the Bohm module will see
that the firmware on the SD card is the same as the one in the module,
and won't update it again.
