# Easy-as-pie Android Decompiler

## Updates

- apktool to 2.2.1 - [Adds Android Nougat support and other misc fixes](http://connortumbleson.com/2016/10/18/apktool-v2-2-1-released/).
- jadx 0.6.1 replacing dex2jar and jd-cmd

## Why
### One stop shop
The motivation is still the same as original:

> I got pretty tired of decompiling Android apps with a bunch of steps that I had to remember all the time. It involved a lot of apktool, dex2jar, and jd-gui; it still confuses me.

### Collocation of source files
Further, even after these steps were complete (usually a combination of dex2jar and JD-GUI), I would be left with disparate sources of information; the decompiled Java would be over here in this directory, while the un-DEXed content would be somewhere else (Really bad for importing into Eclipse!)

I basically wanted to make this generate a tree and source as close as possible to what the original Android developer sees.

## What
apk2gold is basically a small amount of original content (the R.* thing) and a script wrapping some excellent 3rd-party tools. It is designed to be easily installed and to get you the best results for Android app introspection as quickly as possible. The project stands on the shoulders of the following giants:

* **[skylot/jadx](https://github.com/skylot/jadx)**

* **[apktool](https://github.com/iBotPeaches/Apktool)**

## Installation

### Dependencies

You'll need git if you're going to clone. Also, java installed. git is only necessary for cloning the repo. You can also download [zip file](https://github.com/nepalihackers/apk2gold-reloaded/archive/master.zip) instead of cloning.

### Installing

```shell
git clone https://github.com/nepalihackers/apk2gold-reloaded $HOME/.apk2gold-reloaded
echo "export PATH=$PATH:$HOME/.apk2gold-reloaded" >> ~/.bashrc
source ~/.bashrc
```

now, you can run `apk2gold` command anywhere.

## Usage

### Getting the APK
There are different ways to acquire an APK, but the easiest is to just download it from the Play Store and use ES File Explorer to back up the APK (ES File Explorer -> "AppMgr" tab -> long click on app you want -> backup). The APK is now in the 'backups' directory on your SD card. Now you can just USB it over (I like to email it to myself from ES File Explorer itself). More depth can be found at [this SO post](http://stackoverflow.com/questions/12175904/where-can-i-find-the-apk-file-on-my-device-when-i-download-any-app-and-install).

### Decompiling
Actually using my tool easy as pie! Just use:  
`apk2gold <target>.apk`

### Looking at the result
This will create a folder with the APK's name without '.apk' suffix. Everything is in there. There is also an additional directory you may not recognize, `/.smali`, which contains the Smali output from APKTool. Load it up in Eclipse and have fun!  
Note that the result will almost certainly not compile; that's not really the goal. We just want to get an idea of whats happening in the source code, check for malicious shit, etc.
