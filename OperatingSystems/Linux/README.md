## updating .bashrc

`. ~/.bashrc`

## restore your .bashrc:

`cp /etc/skel/.bashrc ~/`

## SSH

ssh access: `ssh user@host`

ssh download: `scp -r user@host:~/directory/`

ssh upload: `scp file.ext user@host:/directory/`

## COPY/MOVE/REMOVE

copy file: `cp file.ext ~/destiny/`

copy folder: `cp -r /folder/ ~/destiny/`

moving file: `mv file.ext ~/destiny/`

moving folder: `mv -r /folder/ ~/destiny/`

remove file: `rm file.ext`

remove folder: `rm -r /folder/`

## SHUTDOWN/REBOOT

shutdown: `sudo shutdown -h now`

reboot: `sudo reboot`


## FIND

find file: `find ~/ -type f -name "filename"`

## STANDARD I/O

`compiler < input.file > output.file`

to append the results: `compiler < input.file >> output.file`

--------------------

[funny side of linux](http://mylinuxbook.com/funny-side-of-linux-command-line)


## TAR.GZ [(source)](http://www.simplehelp.net/2008/12/15/how-to-create-and-extract-zip-tar-targz-and-tarbz2-files-in-linux/)

Good compression while not utilizing too much of the CPU.

`tar -zcvf archive_name.tar.gz directory_to_compress`

To decompress an archive use the following syntax:

`tar -zxvf archive_name.tar.gz`

Extract the files to a different directory:

`tar -zxvf archive_name.tar.gz -C /tmp/extract_here/`

## Extracting general .tar balls

`tar xf archive.tar`



### Creating a shortcut:

`gnome-desktop-item-edit Desktop --create-new`

install if required:

`sudo apt-get install --no-install-recommends gnome-panel`

#### Example: creating a firefox shortcut:

`command: /usr/bin/firefox`




## wget directories

-r : recursive

-nd : prevents creating folders

--reject "foo*" : prevents downloading index.html

`wget -r --no-parent -nd --reject "index.html*" "http://link.com"`

--reject "* .foo*" : prevents downloading all files with .foo extension

`wget -r --no-parent -nd --reject "*.html*" "http://link.com"`

### Frequently used:
`wget -r --no-parent --reject "*.html*" "http://link.com"`


----


* [Linux basic command-line Cheatsheet](#linux_command)

<a name="linux_command"></a>previous filename: linux_command.rst

Linux_Command
==============

| instruction | command line |
|:-----------:|:------------:|
| **[UN]COMPRESS** | |
| extracting tar 	|   ``tar xf archive.tar``   |
| **SSH** | |
| ssh access 			|   ``ssh [user]``   |
| ssh download  		|   ``scp -r [user]:~/[directory]``   |
| ssh upload 			|   ``scp source user@host:dir``   |
| **COPY / MOVE / REMOVE** |
| copy file 			|   ``cp [file] [destination]``   |
| copy folder 		|   ``cp -r [file] [destination]``    |
| moving file 		|   ``mv [foo] ~/file/``   |
| moving folder 		|   ``mv -r [foo] ~/file/``   |
| remove file 		|   ``rm [file]``   |
| remove folder 		|   ``rm -r [folder]``   |
| **SHUTDOWN** | |
| shutdown 			|   ``sudo shutdown -h now``   |
| reboot 				|   ``sudo reboot``   |


links

*  [fun linux](http://mylinuxbook.com/funny-side-of-linux-command-line)


[⇪ back to top](#index)

[↳ go to database](#database)



160724
======

http://askubuntu.com/questions/131601/gpg-error-release-the-following-signatures-were-invalid-badsig
error

I ran this command in the Terminal:

sudo apt-get update
Updating ends with the following error report:

W: A error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: http://extras.ubuntu.com precise Release: The following signatures were invalid: BADSIG 16126D3A3E5C1192 Ubuntu Extras Archive Automatic Signing Key <ftpmaster@ubuntu.com>

W: GPG error: http://ppa.launchpad.net precise Release: The following signatures were invalid: BADSIG 4C1CBC1B69B0E2F4 Launchpad PPA for Jonathan French
W: Failed to fetch http://extras.ubuntu.com/ubuntu/dists/precise/Release  


sudo apt-get clean
sudo mv /var/lib/apt/lists /tmp
sudo mkdir -p /var/lib/apt/lists/partial
sudo apt-get clean
sudo apt-get update


  +
  This message is displaying because the gpg key for that repository is missing in your apt-key database.

  To import the key, open a terminal and enter these commands

  sudo gpg --keyserver hkp://subkeys.pgp.net --recv-keys 16126D3A3E5C1192
  You must replace the alphanumeric part, with the specific key. Make sure the key is one you trust. Any repository with this key, would be able to install any package without warning.

  You would see the following output if the above is successful

  gpg: Total number processed: 1
  gpg:               imported: 1
  Then run this command:

  sudo gpg --export --armor 16126D3A3E5C1192 | sudo apt-key add -
  Note the - sign after add.

  Then sudo apt-get update, you will have no such messages after this.
  +




but the above didnt work

still the error persisted:

    W: GPG error: http://download.opensuse.org ./ Release: The following signatures were invalid: KEYEXPIRED 1436387333



It was suggested to do (i) or (ii)

(i)
http://askubuntu.com/questions/650032/gpg-errorthe-following-signatures-were-invalid-keyexpired

    down vote
    That ppa has been removed and no longer exists. You must find a different source for the packages installed through the samrog131 ppa.

    In the meantime, run the following commands to resolve the situation.

    First, to delete the expired key:

    sudo apt-key del 1436387333
    Then, to delete the ppa:

    sudo rm /etc/apt/sources.list.d/samrog131*
    sudo apt-get clean
    sudo apt-get update
    If you need to add a key see here.

    sudo apt-get upgrade
    You may want to run:

    sudo apt-get dist-upgrade

(ii)
http://askubuntu.com/questions/704172/gpg-error-in-apt-get-update

    What I did to solve my question after rebooting and googling more:

    reboot (Reboot the computer)
    sudo apt-get update (this will give you a warning about expired keys)
    apt-key list | grep expired (as suggested in another post) and I got:
    pub 2048R/E084DAB9 2010-10-19 [expired: 2015-10-18]
    copy the key ID is the bit after the / (in my case E084DAB9)
    sudo apt-key adv --recv-keys --keyserver keys.gnupg.net E084DAB9 (remember to change the key ID of this command to the one you get from your computer)
    sudo apt update
    sudo apt upgrade

Im trying the (ii) option...

I still got the error. So I went to install -f, then again upgrade, then update. This solved...


### Creating a shortcut:

`gnome-desktop-item-edit Desktop --create-new`

install if required:

`sudo apt-get install --no-install-recommends gnome-panel`

#### Example: creating a firefox shortcut:

`command: /usr/bin/firefox`
