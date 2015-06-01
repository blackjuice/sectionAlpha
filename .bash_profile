## source: http://osxdaily.com/2013/02/05/improve-terminal-appearance-mac-os-x/

# create .bash_profile:
`touch .bash_profile`
`vi .bash_profile`

# insert:
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
alias ls='ls -GFh'

# to reload the bash:
`. .bash_profile`

## tips for the color:
To change the colors in the PS1 prompt, change the text between the “\[033[” and the “m\]”.
Nothing means reset to default; number means that color;
number followed by “;1″ means the bright or bold version of that color.

31 – red
32 – green
33 – yellow
34 – blue
35 – magenta
36 – cyan
37 – white

For example, “\[33[34;1m\]” is bold/bright blue.

The special values (e.g. \u for the username, 
\h for the hostname, \w for the current working directory) 
are documented in the “PROMPTING” section of the bash man page.

Don’t like the actual colors displayed
(e.g. blue is hard to read on a black background)?

Change them in Terminal’s preferences (under Settings and the profile being used.)
