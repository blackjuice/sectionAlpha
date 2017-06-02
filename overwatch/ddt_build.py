# import from default python libraries
import sys
# import from custom
from aux_print_py3 import *

# AUXILARY FUNCTIONS
# jump commentary lines on .csv file
def jmpComment(datafileString):
    i = 0
    with open(datafileString) as infile:
        for line in infile:
            i += 1
            if not (line).startswith("//"):
                infile.close(); return i;

# DICTIONARY
# imported from ddt_builder151231
def csv2ddt (datafileString):
    i = jmpComment(datafileString)
    with open(datafileString) as infile:
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

# EXECUTION
datafileString = 'data.csv'
ddt = {}
ddt = csv2ddt(datafileString)
# printing test
print (ddt)
print_ddt (ddt)
print_ddt_sorted_key (ddt)
print_ddt_keys_SCH (ddt)
print_file (datafileString)