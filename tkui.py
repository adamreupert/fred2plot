#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 17:24:04 2021

@author: adam
"""

#puplic imports

import os
#from os import listdir
#from os.path import isfile, join
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
#from scipy import sparse
#from scipy.sparse.linalg import spsolve
from tkinter import *
from tkinter import Tk, Button, Radiobutton, Grid, N, S, W, E, Frame, IntVar, Label, Checkbutton, Entry
import tkinter.filedialog as fd

#local imports
from Methods import xrd_routine
from Methods import echem_routine

def create_frames():
    Master_frame.grid(row=0, column=0, sticky=N)
    for row_index in range(2):
        Grid.rowconfigure(Master_frame, row_index, weight=1)
        for col_index in range(1):
            Grid.columnconfigure(Master_frame, col_index, weight=23)
            
    Methods_frame.grid(row=0, column=0)
    for row_index in range(1):
        Grid.rowconfigure(Methods_frame, row_index, weight=1)
        for col_index in range(8):
            Grid.columnconfigure(Methods_frame, col_index, weight=1)
            
    XRD_frame.grid(row=1, column=0)
    for row_index in range(24):
        Grid.rowconfigure(XRD_frame, row_index, weight=1)
        for col_index in range(24):
            Grid.columnconfigure(XRD_frame, col_index, weight=1)
# have to change similar to XRD for followup menus    
    NMR_frame.grid(row=1, column=0, sticky=N+W)
    for row_index in range(23):
        Grid.rowconfigure(NMR_frame, row_index, weight=1)
        for col_index in range(24):
            Grid.columnconfigure(NMR_frame, col_index, weight=1)
            
    FTIR_frame.grid(row=1, column=0, sticky=N+W)
    for row_index in range(23):
        Grid.rowconfigure(FTIR_frame, row_index, weight=1)
        for col_index in range(24):
            Grid.columnconfigure(FTIR_frame, col_index, weight=1)
            
    Raman_frame.grid(row=1, column=0, sticky=N+W)
    for row_index in range(23):
        Grid.rowconfigure(Raman_frame, row_index, weight=1)
        for col_index in range(23):
            Grid.columnconfigure(Raman_frame, col_index, weight=1)
            
    TGA_DSC_frame.grid(row=1, column=0, sticky=N+W)
    for row_index in range(23):
        Grid.rowconfigure(TGA_DSC_frame, row_index, weight=1)
        for col_index in range(24):
            Grid.columnconfigure(TGA_DSC_frame, col_index, weight=1)
            
    SEM_EDX_frame.grid(row=1, column=0, sticky=N+W)
    for row_index in range(23):
        Grid.rowconfigure(SEM_EDX_frame, row_index, weight=1)
        for col_index in range(24):
            Grid.columnconfigure(SEM_EDX_frame, col_index, weight=1)
            
    EC_frame.grid(row=1, column=0, sticky=N+W)
    for row_index in range(23):
        Grid.rowconfigure(EC_frame, row_index, weight=1)
        for col_index in range(24):
            Grid.columnconfigure(EC_frame, col_index, weight=1)
    
    Config_frame.grid(row=1, column=0, sticky=N+W)
    for row_index in range(23):
        Grid.rowconfigure(Config_frame, row_index, weight=1)
        for col_index in range(24):
            Grid.columnconfigure(Config_frame, col_index, weight=1)

def tab_XRD():
    print('XRD')
    Button_tab_XRD.configure(state="disable")
    Button_tab_NMR.configure(state="normal")
    Button_tab_FTIR.configure(state="normal")
    Button_tab_Raman.configure(state="normal")
    Button_tab_TGA_DSC.configure(state="normal")
    Button_tab_SEM_EDX.configure(state="normal")
    Button_tab_EC.configure(state="normal")
    Button_tab_Config.configure(state="normal")
    XRD_frame.grid()
    NMR_frame.grid_remove()
    FTIR_frame.grid_remove()
    Raman_frame.grid_remove()
    TGA_DSC_frame.grid_remove()
    SEM_EDX_frame.grid_remove()
    EC_frame.grid_remove()
    Config_frame.grid_remove()
    
def tab_NMR():
    print('NMR')
    Button_tab_XRD.configure(state="normal")
    Button_tab_NMR.configure(state="disable")
    Button_tab_FTIR.configure(state="normal")
    Button_tab_Raman.configure(state="normal")
    Button_tab_TGA_DSC.configure(state="normal")
    Button_tab_SEM_EDX.configure(state="normal")
    Button_tab_EC.configure(state="normal")
    Button_tab_Config.configure(state="normal")
    XRD_frame.grid_remove()
    NMR_frame.grid()
    FTIR_frame.grid_remove()
    Raman_frame.grid_remove()
    TGA_DSC_frame.grid_remove()
    SEM_EDX_frame.grid_remove()
    EC_frame.grid_remove()
    Config_frame.grid_remove()

def tab_FTIR():
    print('FT-IR')
    Button_tab_XRD.configure(state="normal")
    Button_tab_NMR.configure(state="normal")
    Button_tab_FTIR.configure(state="disable")
    Button_tab_Raman.configure(state="normal")
    Button_tab_TGA_DSC.configure(state="normal")
    Button_tab_SEM_EDX.configure(state="normal")
    Button_tab_EC.configure(state="normal")
    Button_tab_Config.configure(state="normal")
    XRD_frame.grid_remove()
    NMR_frame.grid_remove()
    FTIR_frame.grid()
    Raman_frame.grid_remove()
    TGA_DSC_frame.grid_remove()
    SEM_EDX_frame.grid_remove()
    EC_frame.grid_remove()
    Config_frame.grid_remove()

def tab_RAMAN():
    print('Raman')
    Button_tab_XRD.configure(state="normal")
    Button_tab_NMR.configure(state="normal")
    Button_tab_FTIR.configure(state="normal")
    Button_tab_Raman.configure(state="disable")
    Button_tab_TGA_DSC.configure(state="normal")
    Button_tab_SEM_EDX.configure(state="normal")
    Button_tab_EC.configure(state="normal")
    Button_tab_Config.configure(state="normal")
    XRD_frame.grid_remove()
    NMR_frame.grid_remove()
    FTIR_frame.grid_remove()
    Raman_frame.grid()
    TGA_DSC_frame.grid_remove()
    SEM_EDX_frame.grid_remove()
    EC_frame.grid_remove()
    Config_frame.grid_remove()
    
def tab_TGA_DSC():
    print('TGA and DSC')
    Button_tab_XRD.configure(state="normal")
    Button_tab_NMR.configure(state="normal")
    Button_tab_FTIR.configure(state="normal")
    Button_tab_Raman.configure(state="normal")
    Button_tab_TGA_DSC.configure(state="disable")
    Button_tab_SEM_EDX.configure(state="normal")
    Button_tab_EC.configure(state="normal")
    Button_tab_Config.configure(state="normal")
    XRD_frame.grid_remove()
    NMR_frame.grid_remove()
    FTIR_frame.grid_remove()
    Raman_frame.grid_remove()
    TGA_DSC_frame.grid()
    SEM_EDX_frame.grid_remove()
    EC_frame.grid_remove()
    Config_frame.grid_remove()

def tab_SEM_EDX():
    print('SEM and EDX')
    Button_tab_XRD.configure(state="normal")
    Button_tab_NMR.configure(state="normal")
    Button_tab_FTIR.configure(state="normal")
    Button_tab_Raman.configure(state="normal")
    Button_tab_TGA_DSC.configure(state="normal")
    Button_tab_SEM_EDX.configure(state="disable")
    Button_tab_EC.configure(state="normal")
    Button_tab_Config.configure(state="normal")
    XRD_frame.grid_remove()
    NMR_frame.grid_remove()
    FTIR_frame.grid_remove()
    Raman_frame.grid_remove()
    TGA_DSC_frame.grid_remove()
    SEM_EDX_frame.grid()
    EC_frame.grid_remove()
    Config_frame.grid_remove()

def tab_EC():
    print('Electrochemical Characterization')
    Button_tab_XRD.configure(state="normal")
    Button_tab_NMR.configure(state="normal")
    Button_tab_FTIR.configure(state="normal")
    Button_tab_Raman.configure(state="normal")
    Button_tab_TGA_DSC.configure(state="normal")
    Button_tab_SEM_EDX.configure(state="normal")
    Button_tab_EC.configure(state="disable")
    Button_tab_Config.configure(state="normal")
    XRD_frame.grid_remove()
    NMR_frame.grid_remove()
    FTIR_frame.grid_remove()
    Raman_frame.grid_remove()
    TGA_DSC_frame.grid_remove()
    SEM_EDX_frame.grid_remove()
    EC_frame.grid()
    Config_frame.grid_remove()
    #echem_routine.csv_convert()
    #echem_routine.csv_condensed()
    #echem_routine.csv_capacity_plot()
    #echem_routine.csv_cycle_plot
    ##echem_routine.normalization_automatic_XRD()
    ##echem_routine.plot()

def tab_Config():
    print('Configuration')
    Button_tab_XRD.configure(state="normal")
    Button_tab_NMR.configure(state="normal")
    Button_tab_FTIR.configure(state="normal")
    Button_tab_Raman.configure(state="normal")
    Button_tab_TGA_DSC.configure(state="normal")
    Button_tab_SEM_EDX.configure(state="normal")
    Button_tab_EC.configure(state="normal")
    Button_tab_Config.configure(state="disable")
    XRD_frame.grid_remove()
    NMR_frame.grid_remove()
    FTIR_frame.grid_remove()
    Raman_frame.grid_remove()
    TGA_DSC_frame.grid_remove()
    SEM_EDX_frame.grid_remove()
    EC_frame.grid_remove()
    Config_frame.grid()

#Functions for XRD menu

def update_baseline_entry_plotoptions():
    if option_baseline.get() == 1:
        Entry_plotoptions_baselambda_XRD['state'] = 'normal'
        Entry_plotoptions_baseasym_XRD['state'] = 'normal'
    if option_baseline.get() == 0:
        Entry_plotoptions_baselambda_XRD['state'] = 'disabled'
        Entry_plotoptions_baseasym_XRD['state'] = 'disabled'

def XRD_load():
    print('Load')
    XRD_import_window = Tk()
    XRD_import_window.withdraw() #use to hide tkinter window
    currdir = os.getcwd()
    impdir = fd.askdirectory(parent=XRD_import_window, initialdir=currdir, title='Please select a import directory')
    if len(impdir) > 0:
        impdir = impdir + '/'
        print(impdir)
        XRD_load.variable = impdir
    XRD_import_window.destroy()
    Label_inputdir_result_XRD['text'] = impdir
    
def XRD_export():
    print('Export')
    XRD_export_window = Tk()
    XRD_export_window.withdraw()
    currdir = os.getcwd()
    expdir = fd.askdirectory(parent=XRD_export_window, initialdir=currdir, title='Please select a export directory')
    if len(expdir) > 0:
        expdir = expdir + '/'
        print(expdir)
        XRD_export.variable = expdir    
    XRD_export_window.destroy()
    Label_exportdir_result_XRD['text'] = expdir

def XRD_generate():
    if Label_inputdir_result_XRD['text'] == 'Nothing selected':
        print('You did not specify import directory')
    elif Label_exportdir_result_XRD['text'] == 'Nothing selected':
        print('You did not specify export directory')
    else:
        print('Fire in the hole!')    
        if option_rename.get():
            print("File is reformated")
            xrd_routine.rename_automatic_XRD(XRD_load.variable, XRD_export.variable)
        if option_baseline.get():
            print("File is baseline substracted")
            #xrd_routine.baseline_substraction_automatic_XRD()
        if option_norm.get():
            print("File is normalized") 
            #xrd_routine.normalization_automatic_XRD()
        if option_svgexp.get():
            print("Image is exported as SVG")
            #xrd_routine.plot()
        if option_pngexp.get():
            print("Image is exported as PNG") 
            #xrd_routine.plot()

def run():
    #Create & Configure root 
    root = Tk()
    root.title('Fred2Plot')
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    
    #Create & Configure frames
    Master_frame=Frame(root)
    Methods_frame=Frame(Master_frame)
    XRD_frame=Frame(Master_frame)
    NMR_frame=Frame(Master_frame)
    FTIR_frame=Frame(Master_frame)
    Raman_frame=Frame(Master_frame)
    TGA_DSC_frame=Frame(Master_frame)
    SEM_EDX_frame=Frame(Master_frame)
    EC_frame=Frame(Master_frame)
    Config_frame=Frame(Master_frame)
    
    create_frames()
    
    XRD_frame.grid()
    NMR_frame.grid_remove()
    FTIR_frame.grid_remove()
    Raman_frame.grid_remove()
    TGA_DSC_frame.grid_remove()
    SEM_EDX_frame.grid_remove()
    EC_frame.grid_remove()
    Config_frame.grid_remove()
    
    
    
    #Creating the widgets, sorted according to the menu
    #Menu for different techniques  
    Button_tab_XRD = Button(Methods_frame, text='XRD', width=25, height = 1, state = "normal", command = tab_XRD)
    Button_tab_NMR = Button(Methods_frame, text='NMR', width=25, height = 1, state = "normal", command = tab_NMR)
    Button_tab_FTIR = Button(Methods_frame, text='FT-IR', width=25, height = 1, state = "normal", command = tab_FTIR)
    Button_tab_Raman = Button(Methods_frame, text='Raman', width=25, height = 1, state = "normal", command = tab_RAMAN)
    Button_tab_TGA_DSC = Button(Methods_frame, text='TGA & DSC', width=25, height = 1, state = "normal", command = tab_TGA_DSC)
    Button_tab_SEM_EDX = Button(Methods_frame, text='SEM & EDX', width=25, height = 1, state = "normal", command = tab_SEM_EDX)
    Button_tab_EC = Button(Methods_frame, text='Electrochem.', width=25, height = 1, state = "normal", command = tab_EC)
    Button_tab_Config = Button(Methods_frame, text='Config', width=25, height = 1, state = "normal", command = tab_Config)
    
    #XRD-Menu and its widgets
    Label_header_XRD = Label(XRD_frame, text='XRD-Menu')
    
    #Greate graph
    x = ['Col A', 'Col B', 'Col C']
    y = [50, 20, 80]
    fig = plt.figure(figsize=(9,6.75))
    plt.bar(x=x, height=y)
    plt.xticks(x, rotation=90)
    #Draw graph in TKinter
    Plotcanvas_XRD = FigureCanvasTkAgg(fig, master=XRD_frame)
    Plotcanvas_XRD.draw()
    
    #Label
    Label_plotformat_XRD = Label(XRD_frame, text='Which kind of plot do you want?')
    
    #RadioButtons
    plotformat = IntVar()
    plotformat.set(1)
    Radiobutton_plotformat_XRD1 = Radiobutton(XRD_frame, text='Single-plot', variable=plotformat, value=1)
    Radiobutton_plotformat_XRD2 = Radiobutton(XRD_frame, text='Multi-plot', variable=plotformat, value=2) 
    Radiobutton_plotformat_XRD3 = Radiobutton(XRD_frame, text='Rietveld-plot', variable=plotformat, value=3) 
    
    #Data processing options
    Label_option_XRD = Label(XRD_frame, text='Data processing options:')
    option_rename = IntVar()
    option_rename.set(1)
    Checkbox_option_rename_XRD = Checkbutton(XRD_frame, text="File reformatting", variable=option_rename)
    option_baseline = IntVar()
    option_baseline.set(1)
    Checkbox_option_baseline_XRD = Checkbutton(XRD_frame, text="Baseline substraction", variable=option_baseline, command=update_baseline_entry_plotoptions)
    option_norm = IntVar()
    option_norm.set(1)
    Checkbox_option_norm_XRD = Checkbutton(XRD_frame, text="Normalization", variable=option_norm)
    option_fileexp = IntVar()
    option_fileexp.set(1)
    Checkbox_option_fileexp_XRD = Checkbutton(XRD_frame, text="Export results as csv file", variable=option_fileexp)
    option_svgexp = IntVar()
    option_svgexp.set(1)
    Checkbox_option_svgexp_XRD = Checkbutton(XRD_frame, text="SVG image export", variable=option_svgexp)
    option_pngexp = IntVar()
    option_pngexp.set(0)
    Checkbox_option_pngexp_XRD = Checkbutton(XRD_frame, text="PNG image export", variable=option_pngexp)
    
    # Options for shaping the plot
    Label_plotoptions_XRD = Label(XRD_frame, text='Plot options:')
    Label_plotoptions_baselambda_XRD = Label(XRD_frame, text='λ (10^2 to 10^9)')
    Entry_plotoptions_baselambda_XRD = Entry(XRD_frame)
    Entry_plotoptions_baselambda_XRD.insert(0, '1000000')
    Label_plotoptions_baseasym_XRD = Label(XRD_frame, text='Asym. (10e-3 to 10e-1)')
    Entry_plotoptions_baseasym_XRD = Entry(XRD_frame)
    Entry_plotoptions_baseasym_XRD.insert(0, '0.001')
    update_baseline_entry_plotoptions()
    Label_plotoptions_x1_XRD = Label(XRD_frame, text='Start X')
    Entry_plotoptions_x1_XRD = Entry(XRD_frame)
    Entry_plotoptions_x1_XRD.insert(0, '0')
    Label_plotoptions_x2_XRD = Label(XRD_frame, text='End X')
    Entry_plotoptions_x2_XRD = Entry(XRD_frame)
    Entry_plotoptions_x2_XRD.insert(0, '60')
    Label_plotoptions_y1_XRD = Label(XRD_frame, text='Start Y')
    Entry_plotoptions_y1_XRD = Entry(XRD_frame)
    Entry_plotoptions_y1_XRD.insert(0, '0')
    Label_plotoptions_y2_XRD = Label(XRD_frame, text='End Y')
    Entry_plotoptions_y2_XRD = Entry(XRD_frame)
    Entry_plotoptions_y2_XRD.insert(0, '1.5')
    
    #Import und export directory
    Button_inputdir_XRD = Button(XRD_frame, text='Load', width=15, height = 1, state = "normal", command = XRD_load)
    Button_exportdir_XRD = Button(XRD_frame, text='Export', width=15, height = 1, state = "normal", command = XRD_export)
    Label_inputdir_XRD = Label(XRD_frame, text='Input-Dir:')
    Label_exportdir_XRD = Label(XRD_frame, text='Export-Dir:')
    Label_inputdir_result_XRD = Label(XRD_frame, text='Nothing selected')
    Label_exportdir_result_XRD = Label(XRD_frame, text='Nothing selected')
    
    #Generate Button
    Button_generate_XRD = Button(XRD_frame, text='Generate', width=15, height = 1, state = "normal", command = XRD_generate)
    
    
    
    
    #Shoving into screen using grid system
    #Menu for different techniques
    Button_tab_XRD.grid(row=0,column=0,sticky=N+S+E+W)
    Button_tab_NMR.grid(row=0,column=1,sticky=N+S+E+W)
    Button_tab_FTIR.grid(row=0,column=2,sticky=N+S+E+W)
    Button_tab_Raman.grid(row=0,column=3,sticky=N+S+E+W)
    Button_tab_TGA_DSC.grid(row=0,column=4,sticky=N+S+E+W)
    Button_tab_SEM_EDX.grid(row=0,column=5,sticky=N+S+E+W)
    Button_tab_EC.grid(row=0,column=6,sticky=N+S+E+W)
    Button_tab_Config.grid(row=0,column=7,sticky=N+S+E+W)
    
    #XRD-Menu and its widgets
    Label_header_XRD.grid(row=0,column=0, columnspan=24, sticky=N+S+E+W)
    Plotcanvas_XRD.get_tk_widget().grid(row=1, column=0, rowspan = 24, columnspan=15, sticky=N+S+E+W)
    Label_plotformat_XRD.grid(row=1,column=15, columnspan=9, sticky=N+S+W)
    Radiobutton_plotformat_XRD1.grid(row=2,column=16,columnspan=2, sticky=N+S+E+W)
    Radiobutton_plotformat_XRD2.grid(row=2,column=19,columnspan=2, sticky=N+S+E+W)
    Radiobutton_plotformat_XRD3.grid(row=2,column=22,columnspan=2, sticky=N+S+E+W)
    Label_option_XRD.grid(row=3,column=15, columnspan=9, sticky=N+S+W)
    Checkbox_option_rename_XRD.grid(row=4,column=16,columnspan=4, sticky=N+S+W)
    Checkbox_option_baseline_XRD.grid(row=4,column=20,columnspan=4, sticky=N+S+W)
    Checkbox_option_norm_XRD.grid(row=5,column=16,columnspan=4, sticky=N+S+W)
    Checkbox_option_fileexp_XRD.grid(row=5,column=20,columnspan=4, sticky=N+S+W)
    Checkbox_option_pngexp_XRD.grid(row=6,column=16,columnspan=4, sticky=N+S+W)
    Checkbox_option_svgexp_XRD.grid(row=6,column=20,columnspan=4, sticky=N+S+W)
    Label_plotoptions_XRD.grid(row=7,column=15, columnspan=9, sticky=N+S+W)
    
    Label_plotoptions_baselambda_XRD.grid(row=8,column=16,columnspan=2, sticky=N+S+W)
    Entry_plotoptions_baselambda_XRD.grid(row=8,column=18,columnspan=2, sticky=N+S+W)
    Label_plotoptions_baseasym_XRD.grid(row=8,column=20,columnspan=2, sticky=N+S+W)
    Entry_plotoptions_baseasym_XRD.grid(row=8,column=22,columnspan=2, sticky=N+S+W)
    
    Label_plotoptions_x1_XRD.grid(row=9,column=16,columnspan=2, sticky=N+S+W)
    Entry_plotoptions_x1_XRD.grid(row=9,column=18,columnspan=2, sticky=N+S+W)
    Label_plotoptions_x2_XRD.grid(row=9,column=20,columnspan=2, sticky=N+S+W)
    Entry_plotoptions_x2_XRD.grid(row=9,column=22,columnspan=2, sticky=N+S+W)
    Label_plotoptions_y1_XRD.grid(row=10,column=16,columnspan=2, sticky=N+S+W)
    Entry_plotoptions_y1_XRD.grid(row=10,column=18,columnspan=2, sticky=N+S+W)
    Label_plotoptions_y2_XRD.grid(row=10,column=20,columnspan=2, sticky=N+S+W)
    Entry_plotoptions_y2_XRD.grid(row=10,column=22,columnspan=2, sticky=N+S+W)
    
    
    
    
    
    
    
    
    
    
    
    Button_inputdir_XRD.grid(row=20,column=16,columnspan=4, sticky=N+S+E+W)
    Button_exportdir_XRD.grid(row=20,column=20,columnspan=4, sticky=N+S+E+W)
    Label_inputdir_XRD.grid(row=21,column=16,columnspan=2, sticky=N+S+W)
    Label_exportdir_XRD.grid(row=22,column=16,columnspan=2, sticky=N+S+W)
    Label_inputdir_result_XRD.grid(row=21,column=18,columnspan=3, sticky=N+S+W)
    Label_exportdir_result_XRD.grid(row=22,column=18,columnspan=3, sticky=N+S+W)
    
    Button_generate_XRD.grid(row=23,column=15,columnspan=9, sticky=N+S+E+W)
    root.mainloop()


if __name__ == "__main__":  
    run()