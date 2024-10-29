# rival-3-fix
fixes the steelseries rival 3 blinking purple issue



ℹ **INFO** 
```
this code is from the official steelseries rival 3 recovery tool just decompiled 
divers and firmware are just for if someone needs it i dont really know
```
```
if you dont want to install python ill have the build in releases, smart screen and 
antiviruses might flag it since it not singed and im not paying for a $200 signature
```

**HOW TO USE**

1. **Install python** 🐍
   - download python from https://python.org (im using python 3.12.6) 
   - in the installer one of the first pages should say add to path, check that
   - Smart filtering to exclude irrelevant listings

     **Alternative**: just install python from the microsoft store *(auto adds to path)*

2. **Install required package** 📦
   - if you have python installed and added to path, open cmd and type in `pip install hidapi`

3. **run main.py** 🏃‍♀️
   - make sure your rival 3 is plugged in when running the file
   - after that your mouse should work but if you unplug/restart your computer youll have to rerun the program 
   - go into SteelSeries GG and where your mouse is it should say `CRITICAL UPDATE: Click to install new firmware.`
   - update the firmware and then the LED on your mousewheel should change from purple/pinkish to orange or any other color

And you're done. Your mouse is fixed. 🔥
