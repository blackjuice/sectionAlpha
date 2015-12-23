# Kivy

## Installing [Kivy](http://kivy.org/docs/installation/installation-linux.html)

Ubuntu / Kubuntu / Xubuntu / Lubuntu (Saucy and above):

`sudo add-apt-repository ppa:kivy-team/kivy`

`sudo apt-get update`

Python2 - python-kivy:

`sudo apt-get install python-kivy`

Python3 - python3-kivy:

`sudo apt-get install python3-kivy`

optionally the examples - kivy-examples:

`sudo apt-get install kivy-examples`

## Start from the Command Line [(guide from main page).](http://kivy.org/docs/installation/installation-linux.html)

We ship some examples that are ready-to-run. However, these examples are packaged inside the package. This means you must first know where easy_install has installed your current kivy package, and then go to the examples directory:

`python -c "import pkg_resources; print(pkg_resources.resource_filename('kivy', '../share/kivy-examples'))"`

And you should have a path similar to:

`/usr/local/lib/python2.6/dist-packages/Kivy-1.0.4_beta-py2.6-linux-x86_64.egg/share/kivy-examples/`

Then you can go to the example directory, and run it:

    # launch touchtracer
    cd <path to kivy-examples>
    cd demo/touchtracer
    python main.py

    # launch pictures
    cd <path to kivy-examples>
    cd demo/pictures
    python main.py

If you are familiar with Unix and symbolic links, you can create a link directly in your home directory for easier access. For example:

1) Get the example path from the command line above

2) Paste into your console:

`ln -s <path to kivy-examples> ~/`

3) Then, you can access to kivy-examples directly in your home directory:

`cd ~/kivy-examples`

If you wish to start your Kivy programs as scripts (by typing ./main.py) or by double-clicking them, you will want to define the correct version of Python by linking to it. Something like:

`sudo ln -s /usr/bin/python2.7 /usr/bin/kivy`

Or, if you are running Kivy inside a virtualenv, link to the Python interpreter for it, like:

`sudo ln -s /home/your_username/Envs/kivy/bin/python2.7 /usr/bin/kivy`

Then, inside each main.py, add a new first line:

`#!/usr/bin/kivy`

NOTE: Beware of Python files stored with Windows-style line endings (CR-LF). Linux will not ignore the <CR> and will try to use it as part of the file name. This makes confusing error messages. Convert to Unix line endings.
