# ![screenshot](http://crunchbang.org/forums/img/avatars/33708.png?m=1375747940) [CrunchBang](http://crunchbang.org/)

## Netbook
Package installed using [UNetbootin](http://unetbootin.sourceforge.net/)

### Partition

| Mount as | size | type | use as | comments |
|:--------:|:----:|:----:|:------:|:--------:|
| /boot | 250MB | Primary | Ext | boot |
| / | 25GB | Logical | Ext4 | i.e. root |
| /home | rest | Logical | Ext4 | file storage |
| swap | 2xRAM | Logical | swap | double of RAM |

## Configuration

* [Black screen, X-shaped cursor on boot:](http://crunchbang.org/forums/viewtopic.php?id=24461&p=3)
``dpkg --configure -a``
* [Fix arrow keys that display A B C D on remote shell](http://vim.wikia.com/wiki/Fix_arrow_keys_that_display_A_B_C_D_on_remote_shell)
``sudo apt-get install vim``
* About [terminator](http://ubuntuforums.org/showthread.php?t=920717)
* [Crunchbang Keyboard Layout](https://blogs.fsfe.org/t.kandler/2013/11/20/crunchbang-keyboard-layout/)
* Add ll command: ``alias ll='ls -l'``
* Set date/time manually: `date --set YYYY-MM-DD` and `date --set 00:00:00`

## Fast config

### Check spec

`sudo dmidecode`

`cat /proc/cpuinfo`

`lscpu`

### [Crunchbang Keyboard Layout](https://blogs.fsfe.org/t.kandler/2013/11/20/crunchbang-keyboard-layout/)

The following shows steps I used to add brazilian-portuguese keyboard input:

``sudo vi /etc/default/keyboard``

To check available languages: `` ls -la /usr/share/X11/xkb/symbols/``. To define shortcuts:

	grp:toggle – Right Alt
	grp:shift_toggle – Two Shift
	grp:ctrl_shift_toggle – Ctrl+Shift
	grp:alt_shift_toggle – Alt+Shift
	grp:ctrl_alt_toggle – Ctrl+Alt
	grp:caps_toggle – CapsLock
	grp:lwin_toggle – Left "Win"
	grp:rwin_toggle – Right "Win"
	grp:menu_toggle – Button "Menu"

So this is how it looks in the end:

	XKBMODEL="pc105"
	XKBLAYOUT="us,br"
	XKBVARIANT=""
	XKBOPTIONS="grp:alt_shift_toggle"
	
To visualize the current layout: 

``sudo vi .config/openbox/autostart``:

Add line:

``fbxkb &``

## Comments

I gave up Lubuntu on my Netbook for the CrunchBang distro for some little annoying issues encountered during the Lubuntu use like:

* not working "option" key;
* couldn't find the hotkey changing options;
* couldn't instal OpenBox;
* ugly interface;

All the reasons above has solutions, possibly, but it became highly incovenient

## Upgrade Crunchbang to BunsenLabs?

Check [this](http://crunchbang.org/forums/viewtopic.php?id=39730)

## Debug

###001) [Solved] No icon images on system:

On start, I receive the following warning box:

``Failed to load pixbuf file: /usr/share/pnmixer/pixmaps/pnmixer-muted.png: Couldn't recognize the image file format for file '/usr/share/pnmixer/pixmaps/pnmixer-muted.png'``

Solving with [forum](http://ubuntuforums.org/showthread.php?t=2111470):

1) Install as root: ``apt-get install libgdk-pixbuf2.0-dev``

2) Execute: ``gdk-pixbuf-query-loaders > /usr/lib/i386-linux-gnu/gdk-pixbuf-2.0/2.10.0/loaders.cache``

Failed attempts:

* Locating: ``locate gdk-pixbuf-query-loaders``;
* ``gdk-pixbuf-query-loaders > /usr/lib/x86_64-linux-gnu/gdk-pixbuf-2.0/2.10.0/loaders.cache``;

### 002) [Śolved] Error while apt-get update and upgrading tint2

	Errors were encountered while processing:
	 /var/cache/apt/archives/tint2_0.11+svn20111022-3_i386.deb
	E: Sub-process /usr/bin/dpkg returned an error code (1)

To solve it, first remove package tint2conf:

	sudo apt-get remove tint2conf
	
Then complete the tint2 install with 

	sudo apt-get -f install

### 003) [Solved] Err http://ppa.launchpad.net wheezy/main Sources (404  Not Found)

	ls /etc/apt/sources.list.d/

Comment the PPA ubuntu sources, then:

	sudo apt-get update
	sudo apt-get dist-upgrade
	sudo apt-get -f install

### 004) [Solved] Linux Boots to terminal

I tried to execute `startx` but it failed. What solved the problem was:

	sudo apt-get install xorg

### 005) [Solved] Setting date/time

Check BIOS clock with `sudo hwclock`. To correct it:

	sudo hwclock --set --date="mm/dd/yy hh:mm:ss"

Then correct system time to the BIOS with `sudo hwclock -s

### 006) [Solved] Change machine name`

Change name to the desired one on:

	/etc/hostname
	/etc/hosts
	  # below 127.0.0.1  localhost
	  #       127.0.1.1  <insert new name here>

Then apply change with: `/etc/init.d/hostname.sh start`
