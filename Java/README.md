# Java

## Install Java [(reference)](http://linuxg.net/how-to-install-java-7-or-java-8-on-ubuntu-debian-raspberry-pis-raspbian/):

	$ sudo add-apt-repository ppa:webupd8team/java

	$ sudo apt-get update

	$ sudo apt-get install oracle-java7-installer

One line command:
``sudo add-apt-repository ppa:webupd8team/java && sudo apt-get update && sudo apt-get install oracle-java7-installer``

### How to install Java 7 on including Debian, Crunchbang, KWheezy and Raspbian:

	$ echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee -a /etc/apt/sources.list

	$ echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee -a /etc/apt/sources.list

	$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886

	$ sudo apt-get update

	$ sudo apt-get install oracle-java7-installer

### How to install Java 8 on including Debian, Crunchbang, KWheezy and Raspbian:

	$ echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee -a /etc/apt/sources.list

	$ echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee -a /etc/apt/sources.list

	$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886

	$ sudo apt-get update

	$ sudo apt-get install oracle-java8-installer