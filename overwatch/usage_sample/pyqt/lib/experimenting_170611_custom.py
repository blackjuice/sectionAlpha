#!/usr/bin/env
#
# Coding by blackjuice, 2017

# Libraries
import sys
import os # folders
import re # regex
import numpy as np
from script001 import *

def is_true(self, bool):
	if (bool == True):
		self.statusBar().showMessage('Message in statusbar is TRUE')
	else:
		self.statusBar().showMessage('Message in statusbar is FALSE')

def statusDate(self):
    msg = getTime()
    self.statusBar().showMessage('Date to be created:', msg)
