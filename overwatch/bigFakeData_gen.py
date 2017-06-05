#!/usr/bin/env
#
# Coding by blackjuice, 2017
#
# About fakeBigDataGen.py
#   program generates N random .csv datas,
#   which N is the number of generated days of matches
#
# run:
# $ python3 fakeBigDataGen.py N
# where N > 0. If N is null, N = 1 by default 

# Libraries
import sys
import numpy as np
import random
import array
# Custom lib
from ddt_build import * # build dictionary

#---------------------------argv---------------------------#
# Data size handler
if len(sys.argv) == 1:
    days = 1
else:
    days = int(sys.argv[-1])


#-------------------------Handlers-------------------------#
# adds .csv to the generated day
def handler_filename(n):
    string = str(n) + ".csv"
    return string

# converts, i.e., m1 to m01
def match_num_format(m_num):
    n = str(m_num)
    if (m_num < 10):
        n = "0" + n
    return n

# return string of nplayers and playerIDs
def handler_players(nplayers, ddt_players):
    nplayers_t  = np.random.randint(1, nplayers) # chooses nplayers
    string      = "," + str(nplayers_t)
    lst         = np.arange(0, nplayers_t)
    np.random.shuffle(lst)

    for k in range(0, nplayers_t):
        string = string + "," + str(lst[k]) # key: ddt_players[ str(lst[k]) ]
    return string

# outputs shuffled array[0..mAll] with status
def handler_status(mAll, mV, mD, mE):
    lst             = np.zeros(mAll, dtype=int)
    lst[ mV:mV+mD ] = 1 # slicing
    lst[ -mE: ]     = 2
    np.random.shuffle(lst) # shuffles lst
    return (lst)


#---------------------------Main---------------------------#
# generates day with generated matches
#   matches ID has a format: mI, where I = 01..mAll
def gen_day_old(days):
    # dictionary of maps
    ddt_maps = {}
    ddt_maps = csv2ddt("csv/maps.csv")
    # dictionary of players
    ddt_players = {}
    ddt_players = csv2ddt("csv/players.csv")
    nplayers = len(ddt_players)
    # array of days
    dates_array = np.arange(100000,100000+days)

    # single day of ranked generator
    for i in dates_array:
        filename = "matches/dummy/" + handler_filename(i)
        f = open(filename, 'w')

        # matches situation generator
        mAll        = np.random.randint(1, 31)
        mV          = np.random.randint(0, mAll + 1)
        mD          = np.random.randint(0, mAll + 1 - mV)
        mE          = mAll - mV - mD
        statuslst   = handler_status(mAll, mV, mD, mE)

        f.write(str(i)  + "," + str(mAll) + "," + str(mV) + "," +
                str(mD) + "," + str(mE)   + "\n")

        # single match generator
        for d in range(0, mAll):
            m_num   = match_num_format(d+1) # formats m_d
            mapID   = random.choice(list(ddt_maps)) # chooses map

            status  = statuslst[d] # gets match's status
            if   (status == 0): status_c = 'v' # converts int to status
            elif (status == 1): status_c = 'd'
            else:               status_c = 'e'

            str_players = handler_players(nplayers, ddt_players) # string of players in the match

            f.write("m"         + m_num + "," +
                    mapID       + ","   +
                    status_c    +
                    str_players + "\n")
        f.close()

#   matches ID are numbered: 0..mAll-1
def gen_day(days):
    # dictionary of maps
    ddt_maps = {}
    ddt_maps = csv2ddt("csv/maps.csv")
    # dictionary of players
    ddt_players = {}
    ddt_players = csv2ddt("csv/players.csv")
    nplayers = len(ddt_players)
    # array of days
    dates_array = np.arange(100000,100000+days)

    # single day of ranked generator
    for i in dates_array:
        filename = "matches/dummy/" + handler_filename(i)
        f = open(filename, 'w')

        # matches situation generator
        mAll        = np.random.randint(1, 31)
        mV          = np.random.randint(0, mAll + 1)
        mD          = np.random.randint(0, mAll + 1 - mV)
        mE          = mAll - mV - mD
        statuslst   = handler_status(mAll, mV, mD, mE)

        f.write(str(i)  + "," + str(mAll) + "," + str(mV) + "," +
                str(mD) + "," + str(mE)   + "\n")

        # single match generator
        for d in range(0, mAll):
            mapID   = random.choice(list(ddt_maps)) # chooses map

            status  = statuslst[d] # gets match's status
            if   (status == 0): status_c = 'v' # converts int to status
            elif (status == 1): status_c = 'd'
            else:               status_c = 'e'

            str_players = handler_players(nplayers, ddt_players) # string of players in the match

            f.write(str(d)  + "," +
                    mapID       + "," +
                    status_c    +
                    str_players + "\n")
        f.close()

#-------------------------Execution------------------------#
gen_day(days)
print(">>", days, "fake matches generated.")