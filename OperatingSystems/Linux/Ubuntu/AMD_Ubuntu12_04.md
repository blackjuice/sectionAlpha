### ATI Catalyst Video Drivers (fglrx) directly from AMD [(source)](http://askubuntu.com/questions/124292/what-is-the-correct-way-to-install-proprietary-ati-catalyst-video-drivers-fglrx/126513#126513)

Download [drivers](http://support.amd.com/en-us/download)

Following these [steps](http://ubuntuforums.org/showthread.php?t=2258205)


### dependency problems

Error processing package fglrx. Package fglrx is not configured yet [(source)](http://askubuntu.com/questions/532645/error-processing-package-fglrx-package-fglrx-is-not-configured-yet)

E: Sub-process /usr/bin/dpkg returned an error code (1)

removing fglrx: `sudo apt-get purge fglrx*`

installing dependencies: `sudo apt-get install -f`

This steps has been tested, but it didn't work [(source)](http://askubuntu.com/questions/78906/ati-amd-proprietary-fglrx-graphics-install-fails-how-can-i-resolve-the-problem)

`sudo apt-get --purge remove fglrx*`

`sudo apt-get install fglrx-updates fglrx-amdcccle-updates`



### From zero to 10:

* At the folder where .run is located: `./amd-driver-installer-14.501.1003-x86.x86_64.run --force`

