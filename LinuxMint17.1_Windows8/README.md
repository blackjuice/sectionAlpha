# [Linux Mint](http://www.linuxmint.com/) 17.1 "Rebecca" - Cinnamon (64-bit)

[reference guide](http://itsfoss.com/guide-install-linux-mint-16-dual-boot-windows/)

	note: Pretty similar to Ubuntu installation guide

## Partition

| Mount as | size | type | use as | comments |
|:--------:|:----:|:----:|:------:|:--------:|
| /boot | 200MB | Primary | Ext | boot |
| / | 15GB | Logical | Ext4 | i.e. root |
| swap | 2xRAM | Logical | swap | double of RAM |
| /home | rest | Logical | Ext4 | file storage |

## Possible issues

* [black screen](http://community.linuxmint.com/tutorial/view/842);