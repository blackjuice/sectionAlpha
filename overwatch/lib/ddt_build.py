# Coding by blackjuice, 2017
#
# About ddt_build.py
#   It receives as input a .csv data
#   and outputs dictionaries of interest

# Libraries
import sys

#------------------------Auxilaries------------------------#
# jump commentary lines from .csv file
def jmpComment(filename):
    i = 0
    with open(filename) as infile:
        for line in infile:
            i += 1
            if not (line).startswith("//"):
                infile.close()
                return i


#------------------------Dictionary------------------------#
# imported from ddt_builder151231
# by blackjuice on pte-python project
def csv2ddt (filename):
    i = jmpComment(filename)
    with open(filename) as infile:
    #with open('data.csv') as infile:
        for j in range(i - 1): #i-1 if whiteline
            line = infile.readline();
        ddt = {}
        for line in infile:
            tmp_array = [x.strip() for x in (line.strip()).split(',')]
            tmp_value = []
            for i in range( 1, len(tmp_array) ):
                tmp_value.insert(i, tmp_array[i])
            ddt.update({tmp_array[0]:tmp_value})
    infile.close()
    return ddt