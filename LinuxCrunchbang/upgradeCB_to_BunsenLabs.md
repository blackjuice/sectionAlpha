# Chunchbang to BunsenLabs

Upgrading Debian 7 (wheezy) to Debian 8 (Jessie)

*references:*

* [linuxveda](http://www.linuxveda.com/2015/04/28/upgrade-from-debian-7-to-debian-8/)
* [crunchbang.org](http://crunchbang.org/forums/viewtopic.php?id=39730)
* [bunsenlabs cb upgrade github](https://github.com/userx-bw/bunsenlabs-cb-upgrade)
* [bunsenlabs forum](https://forums.bunsenlabs.org/viewtopic.php?id=222)

## Get Debian 7 ready for the upgrade

Make sure everything is fully updated:

    sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade

Backup important sections:

* /etc/
* /var/lib/dpkg
* /var/lib/apt/extended_states
    *If you use aptitude, you must also backup: /var/lib/aptitude/pkgstates

And backup the output of the following command:

    dpkg --get-selections "*"

### Backup

For this, we are using **rsync**:

    sudo apt-get install rsync

And to use it:

    rsync -a -v --delete /Directory1/ /Directory2/

    where:
    -a = recursive
    -v = verbose
    --delete = delete redundants

## Remove

    sudo apt-get remove cb-cowpowers cb-welcome tint2conf compton-git cb-configs
    #removing cb-configs too. This is optional

## Change Wheezy to Jessie on /etc/apt/sources.list

Change "wheezy" to "jessie" at `/etc/apt/sources.list`. Also, remove `/etc/apt/preferences`.

Update it:

    sudo apt-get update
    sudo apt-get purge tint2 tint2conf xscreensaver compton-git && sudo apt-get -f install
    sudo apt-get upgrade && sudo apt-get -f install
    sudo apt-get install --reinstall xserver-xorg-input-all
    sudo apt-get dist-upgrade

Now, go to a tty. Enter as root, then go to bunsenlabs script directory:

    tar -xpf master.tar.gz
    cd bunsenlabs-cb-upgrade-master
    ./install-bl8a

(**Note)If the mentioned step fails, we will do it manually. At the tty, dist-upgrade and reboot the system. Again, make sure everything is upgraded, so run dist-upgrade again. Then, run a purge:

    apt-get --purge autoremove

or

    apt-get purge $(dpkg -l | awk '/^rc/ { print $2 }')
    apt-get autoremove

If there are problems with `sudo` later, install it:

    su
    apt-get install sudo

Add user and grant the user sudo permission:
    
    adduser <user> sudo
    visudo
    <user> ALL = (ALL) ALL

## Set up panels:

    sudo apt-get install tint2

Enable the BunsenLabs bunsen-hydrogen and jessie-backports
Set up a file at `/etc/apt/sources.list.d/bunsen.list`:

    deb http://pkg.bunsenlabs.org/debian bunsen-hydrogen main

Set up `/etc/apt/sources.list.d/bunsen-jessie-backports.list`:

    deb http://pkg.bunsenlabs.org/debian jessie-backports main

**upgrade a package**: To upgrade a package to its backports version, target the backports distribution as follows:

    sudo apt-get -t jessie-backports install ${PACKAGE_NAME}

## Signing key

Fetch and verify the repository’s signing key:

    wget https://pkg.bunsenlabs.org/BunsenLabs-RELEASE.asc
    gpg --with-fingerprint BunsenLabs-RELEASE.asc

The key’s fingerprint as displayed by gpg should be identical with the following hexstring:

    3172 4784 0522 7490 BBB7 43E6 A067 3F72 FE62 D9C5 

If that is not the case, you have got the wrong key. Use a safe, non-intercepted internet connection in order to retrieve the correct key file.

Finally, add the key to APT and update the package index:

    sudo apt-key add BunsenLabs-RELEASE.asc
    sudo apt-get update

You may now install bunsen-* packages provided by the repository.

## Now...

    sudo apt-get update

Install compton, obmenu and xfce4-power-manager:

    sudo apt-get install -t jessie-backports compton obmenu xfce4-power-manager-data

Install bunsen-os-release, bunsen-pipemenus and bunsen-themes and icons:

    sudo apt-get install bunsen-os-release bunsen-pipemenus bunsen-faenza-icon-theme bunsen-themes

Update grub:

    sudo update-grub

Edit `~/.config/openbox/autostart` to:

    ## GNOME PolicyKit and Keyring
    eval $(gnome-keyring-daemon -s --components=pkcs11,secrets,ssh,gpg) &
    /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
    ## Set root window colour
    #hsetroot -solid "#2E3436" &

    ## Group start:
    ## 1. nitrogen - restores wallpaper
    ## 2. compositor - start
    ## 3. sleep - give compositor time to start
    ## 4. tint2 panel

    nitrogen --restore &
    compton -Cc &
    (sleep 2 && tint2) &

Edit `~/.config/openbox/menu.xml`: replace all instances of cb- with bl- except for **cb-lock** and **cb-exit**. Comment line: `cb-x-www-browser-pipemenu` (line is around #180).

    <!-- <menu execute="bl-x-www-browser-pipemenu" id="wwwbrowsers" label="WWW Browsers"/> -->

Set themes to Bunsen and icons to Faenza-Dark-Bunsen.

Reboot, grub entry should now read BunsenLabs GNU/Linux.

## Using obmenu-generator (Github) for the Openbox menu

    # Assuming build-essential & git are not already installed
    sudo apt-get install cpanminus build-essential git

    git clone git://github.com/trizen/obmenu-generator
    sudo cp obmenu-generator/obmenu-generator /usr/bin
    sudo cpanm Linux::DesktopFiles
    sudo cpanm Data::Dump

At `~/.config/obmenu-generator/schema.pl`:

    #!/usr/bin/perl

    # obmenu-generator - schema file

    =for comment

        item:      add an item inside the menu               {item => ["command", "label", "icon"]},
        cat:       add a category inside the menu             {cat => ["name", "label", "icon"]},
        sep:       horizontal line separator                  {sep => undef}, {sep => "label"},
        pipe:      a pipe menu entry                         {pipe => ["command", "label", "icon"]},
        raw:       any valid Openbox XML string               {raw => q(xml string)},
        begin_cat: begin of a category                  {begin_cat => ["name", "icon"]},
        end_cat:   end of a category                      {end_cat => undef},
        obgenmenu: generic menu settings                {obgenmenu => ["label", "icon"]},
        exit:      default "Exit" action                     {exit => ["label", "icon"]},

    =cut

    # NOTE:
    #    * Keys and values are case sensitive. Keep all keys lowercase.
    #    * ICON can be a either a direct path to an icon or a valid icon name
    #    * Category names are case insensitive. (X-XFCE and x_xfce are equivalent)

    require "$ENV{HOME}/.config/obmenu-generator/config.pl";

    ## Text editor
    my $editor = $CONFIG->{editor};

    our $SCHEMA = [
      {item => ['gmrun', 'Run Program', 'system-run']},
      
      {sep => undef},
      
      {item => ['terminator', 'Terminal', 'terminal']},
      {item => ['x-www-browser', 'Web Browser', 'web-browser']},
      {item => ['thunar', 'File Manager', 'file-manager']},
      {item => ['geany', 'Text Editor', 'text-editor']},
      {item => ['vlc', 'Media Player', 'media-player']},
      
      {sep => undef},
        
        {cat => ['utility',     'Accessories', 'applications-utilities']},
        {cat => ['development', 'Development', 'applications-development']},
        {cat => ['education',   'Education',   'applications-science']},
        {cat => ['game',        'Games',       'applications-games']},
        {cat => ['graphics',    'Graphics',    'applications-graphics']},
        {cat => ['audiovideo',  'Multimedia',  'applications-multimedia']},
        {cat => ['network',     'Network',     'applications-internet']},
        {cat => ['office',      'Office',      'applications-office']},
        {cat => ['other',       'Other',       'applications-other']},
        {cat => ['settings',    'Settings',    'applications-accessories']},
        {cat => ['system',      'System',      'applications-system']},

        #{cat => ['qt',          'QT Applications',    'qt4logo']},
        #{cat => ['gtk',         'GTK Applications',   'gnome-applications']},
        #{cat => ['x_xfce',      'XFCE Applications',  'applications-other']},
        #{cat => ['gnome',       'GNOME Applications', 'gnome-applications']},
        #{cat => ['consoleonly', 'CLI Applications',   'applications-utilities']},

        #                  LABEL          ICON
        #{begin_cat => ['My category',  'cat-icon']},
        #             ... some items ...
        #{end_cat   => undef},

        #            COMMAND     LABEL        ICON
        #{pipe => ['obbrowser', 'Disk', 'drive-harddisk']},

        ## Generic advanced settings
        {sep       => undef},
        
        {obgenmenu => ['Openbox Settings', 'openbox']},
        
        {sep       => undef},
        
        {pipe => ['cb-places-pipemenu', 'Places', 'places']},
        {pipe => ['cb-recent-files-pipemenu', 'Recent Files', 'recent-files']},
        
      {sep => undef},
      
      {item => ['cb-lock', 'Lock Screen', 'lock-screen']},
      {item => ['cb-exit', 'Exit', 'exit']},
    ]

## Upgrade to Debian 8 server (copied from linuxveda.com)

If you’re planning to upgrade Debian 8 on your VPS, follow these steps. Switch to root user, and install screen:

  su root
  apt-get install screen

Then, start screen session:

  screen

The screen tool will help you to reconnect to your VPS, in case you’re disconnected from it while upgrading.

If you’re disconnected from your VPS, you can re-connect to it using command:

  screen -Dr

Now, edit `/etc/apt/sources.list` file,

  nano /etc/apt/sources.list

Change all instances of wheezy to jessie.

This is how my sources.list file looked after replaced the line wheezy with jessie.

    deb http://mirror.cse.iitk.ac.in/debian/ jessie main
    deb-src http://mirror.cse.iitk.ac.in/debian/ jessie main

    deb http://security.debian.org/ jessie/updates main contrib
    deb-src http://security.debian.org/ jessie/updates main contrib

    # wheezy-updates, previously known as 'volatile'
    deb http://mirror.cse.iitk.ac.in/debian/ jessie-updates main contrib
    deb-src http://mirror.cse.iitk.ac.in/debian/ jessie-updates main contrib

Run the following command to update packages list:

    apt-get update

Then, run the minimal upgrade:

    apt-get upgrade

Finally, run the following command to perform full system upgrade.

    apt-get dist-upgrade

Remove all old and unnecessary packages using commands:

    apt-get purge $(dpkg -l | awk '/^rc/ { print $2 }')
    apt-get autoremove

Finally, reboot your VPS.

    reboot

Done!

### Possible problems after upgrading to Debian 8

If you got any problems with some packages, for example mysql, just install them again.

    sudo apt-get install mysql-server

Still no luck, completely purge and re-install them as shown below.

    sudo apt-get remove --purge mysql-server
    sudo apt-get install mysql-server

While removing mysql-server, the installer will ask you whether to keep the configuration file or not. Just keep the configuration file and continue the installation.