#!/usr/bin/env
#
# Coding by blackjuice, 2017
#
# About fakeBigDataGen.py
#   program generates random data.csv
#   which size of dates can be modified
#
# run:
# $ python3 fakeBigDataGen.py N
# where N > 0. If N is null, N = 1 by default 

# Libraries
import sys
import csv
import numpy as np
import random
# folder creation, error handler
import os
import errno
# Custom lib
from ddt_build import * # build dictionary

# Data size handler
if len(sys.argv) == 1:
    data_size = 1
else:
    data_size = sys.argv[-1]
filename = "dummyCSV/bigData_" + data_size + ".csv"
data_size = int(data_size)

#path = "dummyCSV"
#directory = os.path.dirname(path)

# from https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
        print("dummyCSV folder created")
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
#make_sure_path_exists(path)
def create_folder():
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("dummyCSV folder created")

def test1():
    print()
    # // #date YYMMDD,#total,#victory,#defeat,#draw,v0..vn,d0..dm,dr0..drp,#group,members
    # // 170514,25,12,11,2,route66,lijiang,eichenwalde,numbani,gibraltar,dorado,hollywood,kingsrow,ilios,anubis,eichenwalde,lijiang,kingsrow,oasis,ilios,anubis,volskaya,nepal,anubis,numbani,route66,dorado,nepal,hanamura,hollywood,1,bonecrusher#1561
    # 170514v,12,route66,lijiang,eichenwalde,numbani,gibraltar,dorado,hollywood,kingsrow,ilios,anubis,eichenwalde,lijiang
    # 170514d,11,kingsrow,oasis,ilios,anubis,volskaya,nepal,anubis,numbani,route66,dorado,nepal
    # 170514e,2,hanamura,hollywood
    # 170514p,1,bonecrusher#1561

def data_gen(data_size):
    for i in range(0,data_size):
        rd_date = np.random.randint(140000, high=200000)


def test2(filename, data_size):
    f = open(filename, 'w')
    #f.write("170514v,12,route66,lijiang,eichenwalde,numbani,gibraltar,dorado,hollywood,kingsrow,ilios,anubis,eichenwalde,lijiang\n")
    data_gen(data_size)
    print("file created")
    f.close()
#print(filename)

# String containing list of fictional players
def players_str():
    players_list = ["bonecrusher#1561", "accelcoil#1886", 
                    "mitsuha#1234", "emiyusa#1992",
                    "maosadao#1823", "ashia#1231"]
    return players_list

def test3(filename, data_size):
    # dictionary of maps
    ddt_maps = {}
    ddt_maps = csv2ddt("maps.csv")
    #print_ddt(ddt_maps)

    ddt_players = {}
    ddt_players = csv2ddt("players.csv")
    nplayers = len(ddt_players)
    #print_ddt(ddt_players)

    # calls 
    for i in range(0, data_size):
        # choose date
        rd_date         = np.random.randint(140000, 200000)
        # choose #total matches, #victories, #defeats, #draws
        rd_match_all    = np.random.randint(1, 30)
        rd_match_v      = np.random.randint(0, rd_match_all)
        rd_match_d      = np.random.randint(0, rd_match_all - rd_match_v)
        rd_match_e      = rd_match_all - rd_match_v - rd_match_d


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


test3(filename, data_size)

#data_gen(data_size)