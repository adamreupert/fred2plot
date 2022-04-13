# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:19:54 2022

@author: Adam_Reupert
"""

#Import the required libraries
from tkinter import Tk, Button, Radiobutton, Grid, N, S, W, E, Frame, IntVar, Label, Checkbutton, Entry

def widgetui(mainwindow):
    #print('yippey widdgi')
    widgetgrid = Frame(mainwindow)
    widgetgrid.grid(row=4, column=0, columnspan=7) # Columnspan has to be the same number as there are in total
    
    Button_XRD_plot_widget = Button(widgetgrid, text='Rietveld', width=25, height = 1, state = "normal")
    Button_XRD_plot_widget.grid(row=0,column=0,sticky=N+S)
    widgetgrid.grid_remove()
    return widgetgrid