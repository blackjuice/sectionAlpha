# Installation guide for linux [(source)](http://algs4.cs.princeton.edu/linux/)


## Update your Java

check [this page](https://github.com/blackjuice/sectionAlpha/tree/master/Java) to guide yourself of downloading/updating your Java.

# Install algs4 and debuggers package:

## algs4 package

`wget http://algs4.cs.princeton.edu/code/stdlib.jar && wget http://algs4.cs.princeton.edu/code/algs4.jar && wget http://algs4.cs.princeton.edu/linux/javac-algs4 && wget http://algs4.cs.princeton.edu/linux/java-algs4 && chmod 700 javac-algs4 java-algs4`

moving to ~/bin/

`mv javac-algs4 java-algs4 ~/your/home/directory/algs4/bin`

## debuggers package

`wget http://algs4.cs.princeton.edu/linux/checkstyle.zip && wget http://algs4.cs.princeton.edu/linux/findbugs.zip && unzip checkstyle.zip && unzip findbugs.zip && wget http://algs4.cs.princeton.edu/linux/checkstyle.xml && wget http://algs4.cs.princeton.edu/linux/findbugs.xml && wget http://algs4.cs.princeton.edu/linux/checkstyle-algs4 && wget http://algs4.cs.princeton.edu/linux/findbugs-algs4 && chmod 700 checkstyle-algs4 findbugs-algs4`

moving debuggers to packages and renaming it

`mv checkstyle-algs4 findbugs-algs4 ~/your/home/directory/algs4/bin && mv checkstyle.xml checkstyle-5.5 && mv findbugs.xml findbugs-2.0.3`

## Adding algs4/bin to your PATH environment variable

`export PATH=.:/your/home/directory/algs4/bin:$PATH`

`export CLASSPATH=.:/your/home/directory/algs4/algs4.jar:/your/home/directory/algs4/stdlib.jar`

If the commands above doesn't work, try:

`export PATH=.:$HOME/algs4/bin:$PATH`

`export CLASSPATH=.:$HOME/algs4/algs4.jar:$HOME/algs4/stdlib.jar`

### updating .bashrc

`. ~/.bashrc`

### issues encountered

Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable) [(source)](http://ubuntuforums.org/showthread.php?t=1986288)

to solve this:

`sudo rm /var/lib/apt/lists/* -vf`

`sudo apt-get update`

Unable to locate package oracle-java7-installer [(source)](http://whatizee.blogspot.com.br/2014/07/solved-e-unable-to-locate-package.html)

to solve this:

Enter root mode:

`sudo su`

Adding to deb:

`echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" > /etc/apt/sources.list.d/webupd8team-java.list`

Adding to deb-src:

`echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" >> /etc/apt/sources.list.d/webupd8team-java.list`

Making sure we have the key as well:

`apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886`

Then update:

`apt-get update`

And install Oracle Java:

`apt-get install oracle-java7-installer`

exit root and check Java version to see if it's working:

`java -version`

# Install introcs [(source)](http://introcs.cs.princeton.edu/java/linux/)

## Download the textbook standard libraries stdlib.jar to ~/introcs.

`wget http://introcs.cs.princeton.edu/java/stdlib/stdlib.jar && wget http://introcs.cs.princeton.edu/java/linux/javac-introcs && wget http://introcs.cs.princeton.edu/java/linux/java-introcs && chmod 700 javac-introcs java-introcs`

Moving to bin:

`mv javac-introcs java-introcs ~/your/home/directory/introcs/bin`

## debuggers package

`wget http://introcs.cs.princeton.edu/java/linux/checkstyle.zip && wget http://introcs.cs.princeton.edu/java/linux/findbugs.zip && unzip checkstyle.zip && unzip findbugs.zip && wget http://introcs.cs.princeton.edu/java/linux/checkstyle.xml && wget http://introcs.cs.princeton.edu/java/linux/findbugs.xml && wget http://introcs.cs.princeton.edu/java/linux/checkstyle-introcs && wget http://introcs.cs.princeton.edu/java/linux/findbugs-introcs && chmod 700 checkstyle-introcs findbugs-introcs`

moving debuggers to packages and renaming it

`mv checkstyle-introcs findbugs-introcs ~/your/home/directory/introcs/bin && mv checkstyle.xml checkstyle-5.5 && mv findbugs.xml findbugs-2.0.3 && mv findbugs-2.0.3 checkstyle-5.5 ~/your/home/directory/introcs/bin`

## Add the directory ~/introcs/bin to your PATH environment variable

`export PATH=.:/your/home/directory/introcs/bin:$PATH`

`export CLASSPATH=.:/your/home/directory/introcs/stdlib.jar`

If the commands above doesn't work, try:

`export PATH=.:$HOME/introcs/bin:$PATH`

`export CLASSPATH=.:$HOME/introcs/stdlib.jar`
