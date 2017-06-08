# Overwatch Stats

*creation: 170524*

The following contains Overwatch statistics calculator.

Coding written in `Python`.

<a name="content"></a>
Content:
* [Todo list](#todo);
* [Instance](#instance);
* [Platforms](#platforms);

<a name="todo"></a>
## Todo list

- [X] 000. *-- 170524 --* Write .csv model file
- [X] 001. *-- 170524 --* Read and create hash table from .csv
- [ ] 002. Extract data from ddt (hash table), like how many matches won on M map
- [ ] 003. Plot data with matplot
- [ ] 004. Script for easy matches insertion -> uses log
- [X] 005. *-- 170603 --* Script fake big data generator
- [X] 006. *-- 170602 --* Maps.csv initial structure creation
- [X] 007. *-- 170603 --* [Issue] Each match might contain different number of players. This changes whole mapping and data structure
- [ ] 008. Read each line from a day's match and extract info
- [ ] 009. Create log from a day's match
- [ ] 010. Questions of interest:
    - [ ] 010.0. performance on different game modes
    - [ ] 010.1. in A mode: performance on maps
    - [ ] 010.2. performance with n players
- [ ] 011. Write a `.html` UI example for the demo

<a name="instance"></a>
## Instances

The program should have 3 instances:

1. Reload `stats.log`, which contains all the total stats, ready for the plot's creation. Script responsible: 
    * `reload_log.py`;
2. Update stats after inserting a day of match: the insertion of a day must come from a platform [DISCUSS AVAILABLE TOOLS: web, mobile app, standalone software, script]. The insertion outputs a `YYMMDD.csv`. After a successful file creation, it calls the `load_day.py`, which updates the `stats.log`. Scripts responsible:
    * `insert_day.py`
    * `load_day.py`
3. Plot stats: receives `stats.log` as input and plots all stats of interest. Scripts responsible:
    * `plot_stats.py`

### 1. Reload

This is a developer level instance. This runs through the `/matches/` folder and creates all the dictionaries of each day of match. Ideally this usage will be executed once.

### 2. Update

This is a common user level instance. The client will be inserting data through a easy-to-use platform. 

### 3. Plot

<a name="usage"></a>
## Usage example

The user, `bonecrusher`, will open the main program through a certain [platform](#platform). On this program, the user will enter with the following inputs:
* current date with the `YYMMDD` format, i.e.: if today is 1th of December, 2017, the date format required must be: `171201`;
* 

<a name="platforms"></a>
## Platforms
Possible available platforms:

1. Web-offline;
    * [+] easy usage
    * [+] decent UI (User Interface)
    * [+] will take little time to develop
    * [-] needs php
    * [-] must send data manually
    * [-] will take some time to develop
2. Web-online:
    * [+] easy access
    * [+] decent UI (User Interface)
    * [+] sends emails automatically
    * [-] must have a server
    * [-] will take some time to develop
3. Python standalone program:
    * [+] easy access
    * [-] will take some time to develop
    * [-] must send data manually
4. Android:
    * [+] easy and fast portable access point
    * [-] will take more time to develop
5. Script:
    * [+] will take little time to develop
    * [-] hard access
    * [-] too low-level for a normal user
    * [-] too many requirements to be installed
    * [-] no interface
    * [-] must send data manually

### 1-2) Web application

[Download bootstrap templates.](https://startbootstrap.com/template-categories/all/)

We need `.php` for the `.csv` file creation, which is a bummer since the developer doesn't seems to know anything about it. So the might need to change our approach from a `.html` to a GUI application, which leads us to [[3]](#gui_python).

<a name="gui_python"></a>
### 3) Python standalone program

We have some options here as GUI framework: **Tkinter**, which the developer has some experience; [**PyQT**](https://wiki.python.org/moin/PyQt/Tutorials), with no experience; [**Kivy**](https://kivy.org/#home), with no experience.
