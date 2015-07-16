# Unable to ----?

## Unable to locate package when running apt-get [(source)](http://ubuntuforums.org/showthread.php?t=1908534)

`sudo vi /etc/apt/sources.list`

currently working on 13.10, with **Ubuntu Software > downloadable from the Internet** options all disabled:

`http://ppa.launchpad.net/webupd8team/java/ubuntu`

`http://dl.google.com/linux/chrome/deb/`

`http://ppa.launchpad.net/mumble/release/ubuntu`

independent (source code)

`http://extras.ubuntu.com/ubuntu`

canonical parners (source code)

`http://archive.canonical.com/ubuntu`

## Unable to lock the administration directory (/var/lib/dpkg/) is another process using it? [(source)](http://askubuntu.com/questions/15433/unable-to-lock-the-administration-directory-var-lib-dpkg-is-another-process)

`mkdir ~/beckupVarLib && sudo mv /var/lib/apt/lists/* ~/beckupVarLib && sudo apt-get update`

`sudo rm /var/lib/apt/lists/lock && sudo rm /var/cache/apt/archives/lock`

if the above command doesn't work, try:

`sudo rm /var/lib/dpkg/lock && sudo rm /var/cache/apt/archives/lock`
