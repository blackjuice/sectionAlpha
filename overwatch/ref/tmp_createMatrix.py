# by blackjuice, LuHoTuner, accelcoil, saguahollic & Lucas S.J. Hong
# created on: 160114
# matrix drawer
#import numpy                as np

import numpy                as np
#from print_custom           import * # print_ddt(), print_file(), ...
from builder_ddt151231      import *

# build mini dictionary that labels the columns
# (each column is labeled with a sector)
def build_mini_ddt(ddt):
    # string contains array of sectors & lst_tmp values contains index
    str_tmp = print_ddt_keys_SCH(ddt)
    lst_tmp = [i for i in range( int(ddt["info_nSectors"][0]) ) ]
    # mini dictionary keys are the sectors
    ddt_mini = {el:"" for el in str_tmp};
    i = 0;
    for key in ddt_mini: # add the int as values in sectors
        ddt_mini.update({key:lst_tmp[i]}); i += 1
    return (ddt_mini)

def build_mini_ddt_reversed(ddt):
    # string contains array of sectors
    str_tmp = print_ddt_keys_SCH(ddt)
    # mini dictionary keys are numbered
    lst_tmp = [i for i in range( int(ddt["info_nSectors"][0]) ) ]
    ddt_mini = {el:"" for el in lst_tmp};
    i = 0;
    for key in ddt_mini: # adding [value] "sector" in [key] "i", i an integer
        ddt_mini.update({key:str_tmp[i]}); i += 1
    return (ddt_mini)


# each column receives an sector. And pixels of the column receives
# index_of_the_column + 1 to identify colors
def create_gridASCII(ddt):

    M = np.zeros((24, int(ddt["info_nSectors"][0]) ), dtype=int)
    #M = [[0 for x in xrange( int(ddt["info_nSectors"][0]) )] for x in xrange( 24 )]
    #M = [[0 for x in range( int(ddt["info_nSectors"][0]) )] for x in range( 24 )]

    ddt_mini = {}; index_id = 0;
    for key in ddt:
        if  (not (key).startswith("filename")) and (not (key).startswith("info_")):
            # sector will be labelled with an index (column indicator)
            ddt_mini.update({key:index_id}); index_id += 1;
            i = 2; #lst_2bPainted = [];
            while (i < len(ddt[key])):
                v0 = int( ddt[key][i] ); i += 1;
                v1 = int( ddt[key][i] ); i += 1;

                if (v0 > v1): v1 = v1 + 24
                for j in range (v0, v1):
                    if (j > 23):    M[j - 24][ddt_mini[key]] = ddt_mini[key] + 1; #lst_2bPainted.append( j - 24 )
                    else:           M[j][ddt_mini[key]] = ddt_mini[key] + 1; #lst_2bPainted.append( j )
    #print M
    # defining labels for draw_matplot
    sectors_label = print_ddt_keys_SCH(ddt)
    hours_label = [i for i in range( 24 ) ]
    #draw_matplot(M, sectors_label, hours_label, ddt_mini)
    return (M, sectors_label, hours_label, ddt_mini)

# options: change column
# M is the matrix, ddt_mini has the sectors as key and index as value
def opt_change_column (M, sectors_label, ddt_mini):
    print ("Enter 2 positions to be flipped")
    prev = input()
    next = input()
    #prev, next = [int(j) for j in input().split()]
    print (" ", prev, " <--> ", next)
#    print " ", prev, " <--> ", next

    #M_new = M.copy()
    #M_new[:,[prev, next]] = M_new[:,[next, prev]]
    #print(M); print("before")
    print_gridASCII_VER(24, int(ddt["info_nSectors"][0]), M)
    #print "before"
    M[:,[prev, next]] = M[:,[next, prev]]
    print_gridASCII_VER(24, int(ddt["info_nSectors"][0]), M)
    #print "after"

    ddt_mini_flipped = flip_key_value_ddt(ddt_mini)
    #return (draw_matplot(M, sectors_label, hours_label, ddt_mini)

# flips key, value and returns the new dictionary
def flip_key_value_ddt (ddt):
    ddt_flipped = {}
    for key in ddt:
        ddt_flipped.update({ddt[key]:key})
    #print_ddt(ddt_flipped)
    return (ddt_flipped)

def grid_normalize (M):
    print len(M) # 24 rows
    print len(M[0]) # n_sectors columns
    for x in range( len(M) ):
        for y in range( len(M[0]) ):
            if M[x][y] == y + 2:
                M[x][y] -= 1

    #print_gridASCII_VER(M)
    return M


datafileString = "sch_example151231.txt"
ddt = sch2ddt(datafileString)
M, sectors_label, hours_label, ddt_mini = create_gridASCII(ddt)
#grid_normalize(M)
'''

#print_file(datafileString)
#print_gridASCII_HOR(24, int(ddt["info_nSectors"][0]), M)
print_gridASCII_VER(24, int(ddt["info_nSectors"][0]), M)
opt_change_column (M, sectors_label, ddt_mini)

'''