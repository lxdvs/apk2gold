# Super Easy+Good Android App Decompilation!

# Why
**One stop shop**
I got pretty tired of decompiling Android apps with a bunch of steps that I had to remember all the time.

**Collocation of source files**
Further, even after these steps were complete (usually a combination of dex2jar and JD-GUI), I would be left with disparate sources of information; the decompiled Java would be over here in this directory, while the un-DEXed content would be somewhere else (Really bad for importing into eclipse!)

I basically wanted to make this generate a tree and source as close as possible to what the original Android developer sees.

**Regeneration of R.* References**
One thing that existing decompilers *dont* do is regenerate R references. This project includes a module that does. Which gives you more insight when you're reading source code?
`View v = inflater.inflate(217994357, container, false);`
or
`View v = inflater.inflate(R.layout.result_panel, container, false);`

Now you can easily see and search for what resource is doing what, without needing to file-search R.java.

# What
apk2gold is a collection of (excellent!) 3rd-party tools and original content (the RRegenerator). It is designed to be easily installed and to get you the best results for Android app introspection as quickly as possible. The project stands on the shoulders of the following giants:

**[nviennot/jd-core-java](https://github.com/nviennot/jd-core-java)** (or technically my [fork](https://github.com/lxdvs/jd-core-java) thereof, which actually builds under OSX ;) and by extension, **[JD](http://java.decompiler.free.fr/)**
**[dex2jar](http://code.google.com/p/dex2jar/)**
**[apktool](http://code.google.com/p/android-apktool/)**

# How
