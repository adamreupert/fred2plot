#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 17:24:04 2021

@author: adam
"""

#Import the required libraries
from tkinter import Tk, Button, Radiobutton, Grid, N, S, W, E, Frame, IntVar, Label, Checkbutton, Entry

#Import local files
import Fred_tkui_XRD

def run():
    
    #Create an instance of tkinter frame
    mainwindow= Tk()
    mainwindow.title('Fred2plot')
    
    mainwindow.minsize(1280, 720)
    mainwindow.maxsize(1280, 720)
    #Make widgets resizable by adding weight to the grid 
    for rows in range(1):
        mainwindow.grid_rowconfigure(rows, weight=0)
        for columns in range(8):
            mainwindow.grid_columnconfigure(columns, weight=1)
            
    # Call of 2nd-/widget-layer
    XRD_submenu = Fred_tkui_XRD.submenu_ui(mainwindow)
    
    #Action Functions for Button press of Methods
    def button_push_test():
        print('Hello World!')
    
    def button_push_dummy():
        print('Not implemented')
    
    def button_push_XRD():
        print('XRD-method selected!')
        
        Button_XRD.configure(state="disable")
        XRD_submenu[0].grid()
        Button_NMR.configure(state="normal")
        Button_FT_IR.configure(state="normal")
        Button_Raman.configure(state="normal")
        Button_TGA_DSC.configure(state="normal")
        Button_SEM_EDX.configure(state="normal")
        Button_EC.configure(state="normal")
        Button_Config.configure(state="normal")
        
    def button_push_NMR():
        print('NMR-method selected!')
        Button_XRD.configure(state="normal")
        for widget in XRD_submenu:
            widget.grid_remove()
        Button_NMR.configure(state="disable")
        #NMR_menus.grid()
        Button_FT_IR.configure(state="normal")
        Button_Raman.configure(state="normal")
        Button_TGA_DSC.configure(state="normal")
        Button_SEM_EDX.configure(state="normal")
        Button_EC.configure(state="normal")
        Button_Config.configure(state="normal")
        
            
    #Create widgets / method buttons (1st layer)
    Button_XRD = Button(mainwindow, text='XRD', width=20, height = 1, state = "normal", command = button_push_XRD)
    Button_NMR = Button(mainwindow, text='NMR', width=20, height = 1, state = "normal", command = button_push_NMR)
    Button_FT_IR = Button(mainwindow, text='FT-IR', width=20, height = 1, state = "normal", command = button_push_dummy)
    Button_Raman = Button(mainwindow, text='Raman', width=20, height = 1, state = "normal", command = button_push_dummy)
    Button_TGA_DSC = Button(mainwindow, text='TGA & DSC', width=20, height = 1, state = "normal", command = button_push_dummy)
    Button_SEM_EDX = Button(mainwindow, text='SEM & EDX', width=20, height = 1, state = "normal", command = button_push_dummy)
    Button_EC = Button(mainwindow, text='EC', width=20, height = 1, state = "normal", command = button_push_dummy)
    Button_Config = Button(mainwindow, text='Config', width=20, height = 1, state = "normal", command = button_push_dummy)
    
    
    #Display in UI
    Button_XRD.grid(row=0,column=0,sticky=N+S+E+W)
    Button_NMR.grid(row=0,column=1,sticky=N+S+E+W)
    Button_FT_IR.grid(row=0,column=2,sticky=N+S+E+W)
    Button_Raman.grid(row=0,column=3,sticky=N+S+E+W)
    Button_TGA_DSC.grid(row=0,column=4,sticky=N+S+E+W)
    Button_SEM_EDX.grid(row=0,column=5,sticky=N+S+E+W)
    Button_EC.grid(row=0,column=6,sticky=N+S+E+W)
    Button_Config.grid(row=0,column=7,sticky=N+S+E+W)    
    mainwindow.grid_rowconfigure(1, minsize=25)    
    mainwindow.grid_rowconfigure(2, minsize=10)
    
    
    mainwindow.mainloop()

if __name__ == "__main__":  
    run()



#puplic imports

# import os
# #from os import listdir
# #from os.path import isfile, join
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# #from scipy import sparse
# #from scipy.sparse.linalg import spsolve
# from tkinter import *
# from tkinter import Tk, Button, Radiobutton, Grid, N, S, W, E, Frame, IntVar, Label, Checkbutton, Entry
# import tkinter.filedialog as fd


# def tab_EC():
#     print('Electrochemical Characterization')
#     Button_tab_XRD.configure(state="normal")
#     Button_tab_NMR.configure(state="normal")
#     Button_tab_FTIR.configure(state="normal")
#     Button_tab_Raman.configure(state="normal")
#     Button_tab_TGA_DSC.configure(state="normal")
#     Button_tab_SEM_EDX.configure(state="normal")
#     Button_tab_EC.configure(state="disable")
#     Button_tab_Config.configure(state="normal")
#     XRD_frame.grid_remove()
#     NMR_frame.grid_remove()
#     FTIR_frame.grid_remove()
#     Raman_frame.grid_remove()
#     TGA_DSC_frame.grid_remove()
#     SEM_EDX_frame.grid_remove()
#     EC_frame.grid()
#     Config_frame.grid_remove()
#     #echem_routine.csv_convert()
#     #echem_routine.csv_condensed()
#     #echem_routine.csv_capacity_plot()
#     #echem_routine.csv_cycle_plot
#     ##echem_routine.normalization_automatic_XRD()
#     ##echem_routine.plot()
