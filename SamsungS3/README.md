# Samsung S3 GT-I9300

## Content

* [Issues](#issues);
* [Formatting](#formatting);

## Issues

* [Google Music](#googlemusic);
* [Shuttle Music Player](#shuttle);

## GoogleMusic
### 00. Fix Album art **Google Music**

Delete all my albumthums at ``sdcard > android > data > media``

[> back to Issues](#issues)
[> back to Content](#content)

## Shuttle
http://www.shuttlemusicplayer.com/

### 00. Fix genres and playlists
To fix duplicated and none existing genres and playlists, go to `settings > apps > all > media store` and click `clear data/cache`, then reboot device.

[> back to Issues](#issues)
[> back to Content](#content)

## Formatting

*Currently using dist: RessurectionRemix*

* Download the distribution and google package (*gapps*) on **Internal Storage**;
  * `ResurrectionRemix-M-v5.7.0-20160617-i9300.zip`;
  * `A-GAPPS+6.0.1_14.05.2016_v5.2.zip`;
* Then, root device:
  * Use `Odin_v3.09.zip`;
  * add the `CWM_6.0.4.7_Touch_GT-I9300.tar` package on `AP/PDA`;
  * connect device on USB;
  * power off;
  * press `volume DOWN + power + lock`;
  * then `volume UP` to continue download mode.
* Now we install the packages:
  * press `volume UP + power + lock`;
  * `wipe data`;
  * `wipe cache`;
  * go advanced > `wipe daivik cache`;
  * go to file directory > install first dist;
  * install then gapps;
  * go back and reboot device.

[> back to Content](#content)
