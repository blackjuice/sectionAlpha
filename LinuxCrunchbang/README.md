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

## Fast config

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