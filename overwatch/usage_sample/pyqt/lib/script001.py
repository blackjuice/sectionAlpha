#!/usr/bin/python
#
# Coding by blackjuice, 2017
#
# Get date

# Libraries
import sys
import os # folders
import re # regex
import numpy as np
import time
## dd/mm/yyyy format

def getTime():
    mmdd = time.strftime("%m%d")
    yy = str( int( time.strftime("%Y") ) - 2000 )
    return yy + mmdd

def statusDate(self):
    msg = 'File: ' + getTime() + '.csv'
    self.statusBar().showMessage(msg)
