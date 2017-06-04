#!/usr/bin/env
#
# Coding by blackjuice, 2017

# Libraries
import sys
import csv
import os
# Custom lib
from ddt_build      import * # build dictionary
from matches.lister import * # example of using library from subfolder
                             # subfolder: matches
                             # inside matches, there is an empty file
                             # called __init__.py

#----------------------------------#
#------------EXECUTION-------------#
#----------------------------------#

# returns list of files from subfolder
def files_lst():
    r = []
    for path, dirs, files in os.walk('matches/dummy'):
        for filename in files:
            r.append(os.path.join(path, filename))
    return r

# 170603: opens each file from subfolder
# read each line and extract info from there
# then creates log
def test0():
    f_lst = files_lst()
    nfiles = len(f_lst)
    for filename in f_lst:
        f = open(filename, 'r')
        print(f.read())
        f.close()
#print(filename)
test0()