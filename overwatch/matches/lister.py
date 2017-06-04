#!/usr/bin/env
#
# Coding by blackjuice, 2017

# Libraries
import sys
import os

#----------------------------------#
#------------EXECUTION-------------#
#----------------------------------#

def t1():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(files)