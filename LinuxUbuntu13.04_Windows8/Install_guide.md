##[How to Install/Dual Boot Ubuntu 13.04 and Windows 8](https://www.youtube.com/watch?v=PK7gWIkAY7s)

##Ubuntu on Ultrabok/Vivobook
* [ASUS VivoBook V300CA - Ubuntu 13.04 x64](http://ubuntuforums.org/showthread.php?t=2143119) - Quick report if Ubuntu on Ultrabook/Vivobook works.

* [Ubuntu 14.04 Trusty Tahr + Ultrabook](http://www.dedoimedo.com/computers/ubuntu-trusty-tahr-laptop-ultrabook.html) - Choosing Ubuntu 14.04 Trusty Tahr is a good idea?

* [Getting Ubuntu 14.04 Trusty Tahr](http://releases.ubuntu.com/14.04/)

* [Dual boot: Windows 8 + Ubuntu 14.04](http://www.dedoimedo.com/computers/dual-boot-windows-8-ubuntu.html)

##Installing the pieces!

####Start!
* _F6_ on **nomodeset**
* Try Ubuntu
* Open GParted on Ubuntu to check partition
* Resize and look up for unallocated
* For installation type, choose **Something else**
* Go for **free space**

####Create partition

* ~200 MB for **/boot**
* ~40.000 MB for **/** - Logical for type
* ~140.000 MB for **/home** - Logical for type
* rest for **swap area** - Logical for type


##Possible issues
[trouble installing ubuntu 12.10 on asus windows 8 ultrabook](http://askubuntu.com/questions/327766/trouble-installing-ubuntu-12-10-on-asus-windows-8-ultrabook)

* Click the power button, then Restart, while holding Shift
* Click Advanced Options
* Click UEFI Firmware Settings
* Wait for your computer to restart into BIOS
* Find the Secure Boot Option and disable it from there

It is important you boot into BIOS using this method because otherwise Windows 8 will not shut off completely and you will corrupt it's installation when you install Ubuntu. Once you have done this, install Ubuntu normally. Chances are, it will not be bootable (you will go straight into Windows if you are dual-booting). If not, you are done installing Ubuntu and should not go beyond this point. If this happens, turn Windows off using the Shift+Restart trick and choosing to Power Off. Then, follow these instructions:

* Boot into your LiveCD
* Connect to a WiFi connection point
* Open up Terminal by typing Ctrl+Alt+T
* Run the command:
sudo apt-get update && sudo apt-get install boot-repair && sudo boot-repair
