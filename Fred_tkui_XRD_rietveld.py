# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:19:54 2022

@author: Adam_Reupert
"""

#Import the required libraries
from tkinter import Tk, Button, Radiobutton, Grid, N, S, W, E, Frame, IntVar, Label, Checkbutton, Entry

def widget_ui(mainwindow):
    
    #Create of 3rd-layer grid for the Plot widgets
    widgetgrid = Frame(mainwindow)
    widgetgrid.grid(row=4, column=0, columnspan=7) # Columnspan has to be the same number as there are in total
    
    
    #Create of widgets
    Label_Titeltext = Label(widgetgrid, text= "    Woop Woop    ", font=('Helvetica bold',20))
    Button_XRD_plot_widget = Button(widgetgrid, text='Rietveld', width=25, height = 1, state = "normal")
    
    
    #Show in UI
    Label_Titeltext.grid(row=0,column=0,sticky=N+S+E+W)
    widgetgrid.grid_rowconfigure(1, minsize=10)
    Button_XRD_plot_widget.grid(row=2,column=0,sticky=N+S)
    
    
    #Make widget_ui grid invisible
    #Return grid to be able to change visibility in upper layers
    widgetgrid.grid_remove()
    return widgetgrid