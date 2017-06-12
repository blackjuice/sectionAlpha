#!/usr/bin/env
#
# Coding by blackjuice, 2017
#
# Translates mapID, an integer, to the map's name

# Libraries
import sys

def format_match(lst, ddt_maps, ddt_gmodes, ddt_players):
    if   (lst[1] == '0'): status = 'Victory' # converts int to status
    elif (lst[1] == '1'): status = 'Defeat'
    else:                 status = 'Draw'

    print("     map:",          ddt_maps[lst[0]][2])
    print("     status:",       status)
    print("     nplayers: ",    lst[2])
    for i in range(3, 3 + int(lst[2])):
        print("     ", ddt_players[str(lst[i])])

def which_map(i, ddt):
    print(ddt[str(i)][2])

def which_mode(i, ddt):
    print(ddt[str(i)][0])

#def get_info_match(lst, ddt_maps, ddt_gmodes, ddt_players):
