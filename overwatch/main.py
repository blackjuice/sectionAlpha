#!/usr/bin/env
#
# Coding by blackjuice, 2017

# Libraries
import sys
import os # folders
import re # regex
# Custom lib
from lib.ddt_build  import * # builds dictionary
from lib.ddt_print  import * # prints dictionary
from lib.match_read import *

#------------------------Auxilaries------------------------#
# returns list of files from subfolder
def files_lst():
    r = []
    for path, dirs, files in os.walk('matches/dummy'):
        for filename in files:
            r.append(os.path.join(path, filename))
    return r

# removes file's path and extension
def strip_filename(filename):
    return re.sub('matches/dummy/|.csv', '', filename)

# EXTRACTING DATA FROM ONE FILE
def read_file(filename, ddt_gmodes, ddt_maps, ddt_players):
    # day analysis
    ddt = {}
    ddt = csv2ddt(filename)

    # gets mAll, mV, mD, mE
    key0 = strip_filename(filename)
    mAll = int(ddt[key0][0])
    mV   = int(ddt[key0][1])
    mD   = int(ddt[key0][2])
    mE   = int(ddt[key0][3])

    # runs through matches
    #for i in range(0, mAll):
        #print(" match:", i)
        #translate_all(ddt[str(i)], ddt_maps, ddt_gmodes, ddt_players)

    #return (tAll, tV, tD, tE)
    return (mAll, mV, mD, mE)
    #which_map(2, ddt_maps)
    #print(ddt_gmodes[0])


#---------------------------read_files---------------------------#
def read_files(ddt_gmodes, ddt_maps, ddt_players):
    all_files = files_lst() # get a list of all files
    nfiles = len(all_files) # total files

    tAll, tV, tD, tE = 0, 0, 0, 0

    # run through each file from the list
    for file_i in all_files:
        #print(">> DATE:", strip_filename(file_i))
        mAll, mV, mD, mE = read_file(file_i, ddt_gmodes, ddt_maps, ddt_players)
        #print(tAll, tV, tD, tE)

        tAll += mAll
        tV   += mV
        tD   += mD
        tE   += mE
        #print(tAll, tV, tD, tE)

    pV = '{:.1%}'.format(tV/tAll)
    pD = '{:.1%}'.format(tD/tAll)
    pE = '{:.1%}'.format(tE/tAll)

    print("Total matches read:", nfiles)
    print(pV, pD, pE)


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

filename = "matches/dummy/170000.csv"
#read_file(filename, ddt_gmodes, ddt_maps, ddt_players)
read_files(ddt_gmodes, ddt_maps, ddt_players)
