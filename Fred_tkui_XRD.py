#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 17:24:04 2021

@author: adam
"""

#Import the required libraries
from tkinter import Tk, Button, Radiobutton, Grid, N, S, W, E, Frame, IntVar, Label, Checkbutton, Entry


def menus(mainwindow):
    print('Yippey')
    XRD_submethods_frame=Frame(mainwindow)
    XRD_submethods_frame.grid(row=2, column=0, columnspan=3) # Columnspan has to be the same number as there are submenus
    XRD_plotmenu_frame=Frame(mainwindow)
    XRD_plotmenu_frame.grid(row=4, column=0, columnspan=7) # Columnspan has to be the same number as there are in total
    
    Button_XRD_rietveld = Button(XRD_submethods_frame, text='Rietveld', width=25, height = 1, state = "normal")
    Button_XRD_rietveld.grid(row=0,column=1,sticky=N+S)
    Button_XRD_pdf = Button(XRD_submethods_frame, text='PDF', width=25, height = 1, state = "normal")
    Button_XRD_pdf.grid(row=0,column=2,sticky=N+S)
    XRD_submethods_frame.grid_remove()
    
    
    #plotmenu
    Button_XRD5 = Button(XRD_plotmenu_frame, text='Plot', width=25, height = 1, state = "normal")
    Button_XRD5.grid(row=0,column=0,sticky=N+S)
    Button_XRD_plot = Button(XRD_submethods_frame, text='Plot', width=25, height = 1, state = "normal", command = XRD_plotmenu_frame.grid())
    Button_XRD_plot.grid(row=0,column=0,sticky=N+S)
    XRD_plotmenu_frame.grid_remove()
    return XRD_submethods_frame
    
