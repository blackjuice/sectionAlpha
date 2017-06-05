#!/usr/bin/env
#
# Coding by blackjuice, 2017

# Libraries
import sys
import os # folders
import re # regex
# Custom lib
from lib.ddt_build      import * # build dictionary
from matches.lister import * # example of using library from subfolder
                             # subfolder: matches
                             # inside matches, there is an empty file
                             # called __init__.py
from lib.reader_match import *

#------------------------Auxilaries------------------------#
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
    all_files = files_lst() # get a list of all files
    nfiles = len(all_files) # total files
    # run through each file from the list
    for file_i in all_files:
        f = open(file_i, 'r')
        print(f.read())
        f.close()

# read one file and print each line
def test_one():
    filename = "matches/dummy/100249.csv"
    f = open(filename, 'r')
    
    with open(filename) as f:
        line = f.readlines()
        line = [x.strip() for x in line] # remove \n
        #print(line[0])
        print(line[0][1])
    f.close()

# removes file's path and extension
def strip_filename(filename):
    #cp = re.sub('matches/dummy/|.csv', '', filename)
    #return cp
    return re.sub('matches/dummy/|.csv', '', filename)


# EXTRACTING DATA FROM ONE FILE
def test1(filename, ddt_gmodes, ddt_maps, ddt_players):
    # day analysis
    ddt = {}
    ddt = csv2ddt(filename)
    #print_ddt(ddt)

    # gets mAll, mV, mD, mE
    key0 = strip_filename(filename)
    mAll = int(ddt[key0][0])
    mV   = int(ddt[key0][1])
    mD   = int(ddt[key0][2])
    mE   = int(ddt[key0][3])
    print(mAll, mV, mD, mE)
    #print(len(ddt[key0]))

    # runs through matches
    for i in range(0, mAll):
        print(">> match:", i)
        translate_all(ddt[str(i)], ddt_maps, ddt_gmodes, ddt_players)

    #which_map(2, ddt_maps)
    #print(ddt_gmodes[0])

#---------------------------Main---------------------------#
def main():
    all_files = files_lst() # get a list of all files
    nfiles = len(all_files) # total files


    # run through each file from the list
    for file_i in all_files:
        test1(file_i)
    print(">>>", nfiles)


#-------------------------Execution------------------------#
# dictionary of maps
ddt_maps    = {}
ddt_maps    = csv2ddt("csv/maps.csv")
nmaps       = len(ddt_maps)

ddt_gmodes  = {}
ddt_gmodes  = csv2ddt("csv/game_mode.csv")
ngmodes     = len(ddt_gmodes)

ddt_players = {}
ddt_players = csv2ddt("csv/players.csv")
nplayers    = len(ddt_players)

filename = "matches/dummy/100000.csv"
test1(filename, ddt_gmodes, ddt_maps, ddt_players)
#print(ddt_gmodes['0'])
#print(strip_filename(filename))
#test0()
#test_one()
#main()