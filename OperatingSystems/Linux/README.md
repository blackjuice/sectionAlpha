# Content

* [Basic command lines](#commands);
* [Issues encountered and countered](#issues);
* [Extra fun commands](http://mylinuxbook.com/funny-side-of-linux-command-line).
* [Dot_Files](#dotfiles): favorite configuration on dot files;

## Commands

| function                        | command line |
|:--------------------------------|:-------------|
| **TAR BALLS**                   | ------------ |
| *COMPRESS*                      | |
| Good compression with less CPU  | `tar -zcvf archive_name.tar.gz directory_to_compress` |
| *DECOMPRESS*                    | |
| Extract `.tar` balls            | `tar xf archive.tar` |
| Extract alternative             | `tar -zxvf archive_name.tar.gz` |
| Extract to different directory  | `tar -zxvf archive_name.tar.gz -C /tmp/extract_here/` |
| **SSH**         | ------------ |
| ssh access 			| `ssh [user]`                    |
| ssh download  	| `scp -r [user]:~/[directory]`   |
| ssh upload 			| `scp source user@host:dir`      |
| **COPY / MOVE / REMOVE**  | ------------ |
| copy file 			          | `cp [file] [destination]`     |
| copy folder 		          | `cp -r [file] [destination]`  |
| moving file 		          | `mv [foo] ~/file/`            |
| moving folder 		        | `mv -r [foo] ~/file/`         |
| remove file 		          | `rm [file]`                   |
| remove folder 		        | `rm -r [folder]`              |
| **SHUTDOWN**  | |
| shutdown 			| `sudo shutdown -h now` |
| reboot 				| `sudo reboot`          |
| **WGET**                                            | ------------ |
| prevents downloading `foo*`, example `index.html`   | `wget -r --no-parent -nd --reject "index.html*" "http://link.com"` |
| prevents downloading all files with .foo extension  | `wget -r --no-parent -nd --reject "*.html*" "http://link.com"` |
| recursive                                           | `-r`   |
| prevents creating folders                           | `-nd`  |
| frequently used                                     | `wget -r --no-parent --reject "*.html*" "http://link.com"` |
| **CREATE SHORCUT**    | ------------ |
| create a shorcut      | `gnome-desktop-item-edit Desktop --create-new` |
| install if required   | `sudo apt-get install --no-install-recommends gnome-panel` |
| example: creating a firefox shortcut | `command: /usr/bin/firefox` |
| **.BASHRC**           | ------------ |
| updating .bashrc      | `. ~/.bashrc`             |
| restore your .bashrc  | `cp /etc/skel/.bashrc ~/` |
| **FIND**  | ------------ |
| find file | `find ~/ -type f -name "filename"` |
| **I/O**               | ------------ |
| standard input/output | `compiler < input.file > output.file`   |
| to append the results | `compiler < input.file >> output.file`  |

[> back to Content](#content)

## Issues

* [160724](#160724)

[> back to Content](#content)

## 160724

After the usual update:

    sudo apt-get update

I received a similar error:

    W: A error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: http://extras.ubuntu.com precise Release: The following signatures were invalid: BADSIG 16126D3A3E5C1192

    W: Failed to fetch http://extras.ubuntu.com/ubuntu/dists/precise/Release

It was suggested on this [forum](http://askubuntu.com/questions/131601/gpg-error-release-the-following-signatures-were-invalid-badsig) to run:

    sudo apt-get clean
    sudo mv /var/lib/apt/lists /tmp
    sudo mkdir -p /var/lib/apt/lists/partial
    sudo apt-get clean
    sudo apt-get update

But still the error persisted (similar error):

    W: GPG error: http://download.opensuse.org ./ Release: The following signatures were invalid: KEYEXPIRED 1436387333

After digging a little bit more, we got 2 options:
* [(i)](http://askubuntu.com/questions/650032/gpg-errorthe-following-signatures-were-invalid-keyexpired
);
  *   We delete the expired key:

          sudo apt-key del 1436387333

      Then, to delete the ppa:

          sudo rm /etc/apt/sources.list.d/samrog131*
          sudo apt-get clean
          sudo apt-get update

      If you need to add a key see here.

          sudo apt-get upgrade

      You may want to run:

          sudo apt-get dist-upgrade

* [(ii)](http://askubuntu.com/questions/704172/gpg-error-in-apt-get-update):
  *     reboot (Reboot the computer)
        sudo apt-get update (this will give you a warning about expired keys)
        apt-key list | grep expired
        pub 2048R/E084DAB9 2010-10-19 [expired: 2015-10-18]

    copy the key ID is the bit after the / (in my case E084DAB9)

        sudo apt-key adv --recv-keys --keyserver keys.gnupg.net E084DAB9 (THIS ONE DIDN'T WORK)
        sudo apt update
        sudo apt upgrade

We went for the (ii) option, but we still got the error.
So we went to `install -f`, then again `sudo apt upgrade`, then `sudo apt update`. This solved the problem.

[> back to Issues](#issues)
[> back to Content](#content)


## DotFiles

## .bashrc

Pretty colors on bash profile:

    # COLORS
    # terminal background color = #160C1F
    # for one line
    PS1='\[\033[1m\033[32m\]\u@\h \w\[\033[0m\]\$ '
    # for two lines
    PS1='\[\e[1;32m\]\H\[\e[0m\] :: \[\e[1;30m\]\d\[\e[0m\] \@ :: \[\e[1;33m\]\w\n\[\e[1;34m\]\u $ \[\033[0m\]'

Some custom alias and specific path for custom scripts:

    # Custom
    #-----------------------------------------
    # taking commands on custom created scripts
    export PATH=.:/home/commander/bin/scripts:$PATH
    export PATH=.:/usr/racket/bin:$PATH

    # aliases
    # Check for Debian version
    alias tellmedebianversion='lsb_release -a'

    # shutdown
    alias shutdown='sudo shutdown -h now'

    # reboot
    alias restart='sudo reboot'

    # exit terminal
    alias bye='exit'

    # backstep folder
    alias back='cd ..'

    # .bashrc
    alias bashvi='cd && vi .bashrc'
    alias bashreload='cd && . ~/.bashrc'

    alias sourcevi='cd && sudo vi /etc/apt/sources.list'

    # git
    alias gitadd='git add -A && git commit -a && git push origin master'
    alias gitpull='git pull origin master'

    # apt-get
    alias aptupdate='sudo apt-get update'
    alias aptupgrade='sudo apt-get upgrade'
    alias aptinstallf='sudo apt-get install -f'

## .vimrc

Enable colors for vim and converting tabs to 4 spaces.

    " colors on
    syntax on
    " thanks to http://stackoverflow.com/questions/234564/tab-key-4-spaces-and-auto-indent-after-curly-braces-in-vim
    filetype plugin indent on
    " show existing tab with 4 spaces width
    set tabstop = 4
    " when indenting with '>', use 4 spaces width
    set shiftwidth = 4
    " On pressing tab, insert 4 spaces
    set expandtab

## .inputrc

    $include /etc/inputrc

    # for line seach
    "\e[A": history-search-backward
    "\e[B": history-search-forward
    "\e[C": forward-char
    "\e[D": backward-char

    # stop line bell
    set bell-style none

[> back to Content](#content)