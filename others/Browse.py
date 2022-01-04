# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 12:19:34 2021

@author: pt0042
"""

from tkinter import *
import tkinter.filedialog as fd
import os

root = Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
tempdir = fd.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
if len(tempdir) > 0:
    print("You chose %s" % tempdir)