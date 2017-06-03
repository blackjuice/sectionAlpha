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
import csv
import numpy as np
import random
import array
# folder creation, error handler
import os
import errno
# Custom lib
from ddt_build import * # build dictionary

# Data size handler
if len(sys.argv) == 1:
    days = 1
else:
    days = int(sys.argv[-1])
#filename = "matches/dummy/" + days + ".csv"
#days = int(days)
#path = "dummyCSV"
#directory = os.path.dirname(path)

def gen_date(days):
    for i in range(0,days):
        rd_date = np.random.randint(140000, high=200000)

def test2(filename, days):
    f = open(filename, 'w')
    #f.write("170514v,12,route66,lijiang,eichenwalde,numbani,gibraltar,dorado,hollywood,kingsrow,ilios,anubis,eichenwalde,lijiang\n")
    gen_date(days)
    print("file created")
    f.close()
#print(filename)

# String containing list of fictional players
def players_str():
    players_list = ["bonecrusher#1561", "accelcoil#1886", 
                    "mitsuha#1234", "emiyusa#1992",
                    "maosadao#1823", "ashia#1231"]
    return players_list

def test3(filename, days):
    # dictionary of maps
    ddt_maps = {}
    ddt_maps = csv2ddt("csv_maps.csv")
    #print_ddt(ddt_maps)

    ddt_players = {}
    ddt_players = csv2ddt("csv_players.csv")
    nplayers = len(ddt_players)
    #print_ddt(ddt_players)

    # calls 
    for i in range(0, days):
        # choose date
        rd_date         = np.random.randint(140000, 200000)
        # choose #total matches, #victories, #defeats, #draws
        rd_match_all    = np.random.randint(1, 30)
        rd_match_v      = np.random.randint(0, rd_match_all)
        rd_match_d      = np.random.randint(0, rd_match_all - rd_match_v)
        rd_match_e      = rd_match_all - rd_match_v - rd_match_d
        print ("line0: ", rd_match_all, rd_match_v, rd_match_d, rd_match_e)

        print("number of v: ", rd_match_v)
        str_single_match = ""
        # for each match, choose map, #total players, #player_id
        if (rd_match_v > 0):
            for j in range(0, rd_match_v):
                single_map      = random.choice(list(ddt_maps))
                #print("     single_map choosen:", single_map)
                rd_player_all   = np.random.randint(1, nplayers)
                # write
                str_single_match = str(single_map) + "," + str(rd_player_all)
                str_players_id = ""
                for k in range(0, rd_player_all):
                    rd_player_id = random.choice(list(ddt_players))
                    str_players_id = str(str_players_id) + "," + str(rd_player_id)
                #print(str_players_id)
                str_single_match = str_single_match + str_players_id
                print("     str_single_match = ", str_single_match)
#test3(filename, days)
#gen_date(days)


def gen_day_test(days):
    dates_array = np.arange(100000,100000+days)
    check = False
    for i in dates_array:
        mAll = 10
        mV      = np.random.randint(0, mAll + 1)
        mD      = np.random.randint(0, mAll + 1 - mV)
        mE      = mAll - mV - mD

        status = 0
        nplayers = 0
        playerID = 0
        mapID = 0

        mAll_question = mV + mD + mE
        if (mAll == mAll_question): check = True
        else: check = False
    print (check)
#gen_day_test(days)

# converts, i.e., m1 to m01
def match_num_format(m_num):
    n = str(m_num)
    if (m_num < 10):
        n = "0" + str(m_num)
    return n

# return string of nplayers and playerIDs
def handler_players(nplayers, ddt_players):
    nplayers_t  = np.random.randint(1, nplayers) # chooses nplayers
    lst         = np.arange(0, nplayers_t)
    np.random.shuffle(lst)
    string      = "," + str(nplayers_t)

    for k in range(0, nplayers_t):
        string = string + "," + str(lst[k]) # key: ddt_players[ str(lst[k]) ]
    return string

def handler_status1(mAll, mV, mD, mE):
    lst = []
    for i in range(0, mAll):
        while(mV != 0):
            lst[i] = "v"
            mV = mV - 1
        while(mD != 0):
            lst[i] = "d"
            mD = mD - 1
        while(mE != 0):
            lst[i] = "d"
            mE = mE - 1
    print (lst)
    return np.random.shuffle(lst)

def handler_status2(mAll, mV, mD, mE):
    lst_str = []
    lst = np.zeros(mAll, dtype=int)
    lst[ mV:mV+mD ] = 1
    lst[ -mE: ]     = 2

    for i in range(0,mAll):
        if   (lst[i] == 0): lst_str[i] = 'v'
        elif (lst[i] == 1): lst_str[i] = 'd'
        else:               lst_str[i] = 'e'
    print (lst_str)

# outputs shuffled array[0..mAll] with status
def handler_status(mAll, mV, mD, mE):
    lst             = np.zeros(mAll, dtype=int)
    lst[ mV:mV+mD ] = 1 # slicing
    lst[ -mE: ]     = 2
    np.random.shuffle(lst) # shuffles lst
    return (lst)

# generates day with generated matches
def gen_day(days):
    # dictionary of maps
    ddt_maps = {}
    ddt_maps = csv2ddt("csv_maps.csv")

    # dictionary of players
    ddt_players = {}
    ddt_players = csv2ddt("csv_players.csv")
    nplayers = len(ddt_players)
    #print_ddt(ddt_players)

    dates_array = np.arange(100000,100000+days)
    #print(dates_array)

    # single day of ranked generator
    for i in dates_array:
        #print ("date:", i)

        # matches situation generator
        mAll        = np.random.randint(1, 31)
        mV          = np.random.randint(0, mAll + 1)
        mD          = np.random.randint(0, mAll + 1 - mV)
        mE          = mAll - mV - mD
        statuslst   = handler_status(mAll, mV, mD, mE)
        print ("    ", mAll, mV, mD, mE)

        # single match generator
        for d in range(0, mAll):
            m_num   = match_num_format(d+1) # formats m_d
            mapID   = random.choice(list(ddt_maps)) # chooses map

            status  = statuslst[d] # gets match's status
            if   (status == 0): status_c = 'v' # converts int to status
            elif (status == 1): status_c = 'd'
            else:               status_c = 'e'

            str_players = handler_players(nplayers, ddt_players) # string of players in the match

            print("     m" + m_num + "," +
                mapID + "," +
                status_c +
                str_players)
gen_day(days)
