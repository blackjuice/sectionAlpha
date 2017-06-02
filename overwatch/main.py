#!/usr/bin/env
#
# Coding by blackjuice, 2017

# Libraries
import sys
import csv
# Custom lib
from ddt_build import * # build dictionary

#----------------------------------#
#------------EXECUTION-------------#
#----------------------------------#
# check default input file
if len(sys.argv) == 1:
    filename = 'data.csv'
else:
    filename = sys.argv[-1]

# create empty dictionary
ddt_main = {}

def test1():

    ddt_main = csv2ddt(filename)
    # printing test
    print (ddt)
    print_ddt (ddt)
    print_ddt_sorted_key (ddt)
    print_ddt_keys_SCH (ddt)
    print_file (filename)