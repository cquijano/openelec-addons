# openelec-addons
---
## addons for openelec

### Build Instructions

* Build OpenElec from source [per these instructions](http://wiki.openelec.tv/index.php?title=Compile_from_source) on the wiki.
* Referencing [these other instructions for building an Addon](http://wiki.openelec.tv/index.php?title=How_to_make_OpenELEC_addon_-_on_MuMuDVB_sample), also from the wiki.
* Clone this repo into the `OpenELEC.tv` directory you just built in. This will put the addon code into `packages/addons/`, which is where it needs to be to be found in the next step.
* Still inside the `OpenELEC.tv` directory, run the following, with your appropriate `PROJECT` and `ARCH`:
```
PROJECT=Generic ARCH=i386 ./scripts/create_addon automatic
```
* This will produce a new addon zip under `OpenELEC.tv/target`, depending on your `PROJECT` and `ARCH`.
* Now you can install the addon by expanding the zip into `/storage/.xbmc/addons` on your OpenELEC box, but perhaps there's a better way to do this.
* Finally, you can configure Automatic by editing the conf file inside the addon directory. You can test your configuration by running the .start and .stop scripts manually until your configuration works.
