#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 17:24:04 2021

@author: adam
"""

#Import the required libraries
from tkinter import Tk, Button, Radiobutton, Grid, N, S, W, E, Frame, IntVar, Label, Checkbutton, Entry

#Import local files
import Fred_tkui_XRD_plot
import Fred_tkui_XRD_rietveld
import Fred_tkui_XRD_pdf

def submenu_ui(mainwindow):    
    
    
    
    #Create of 2nd-layer grid for the submenu grid
    XRD_submethods_frame=Frame(mainwindow)
    XRD_submethods_frame.grid(row=1, column=0, columnspan=3, sticky=N+S+E+W) # Columnspan has to be the same number as there are submenus  
    #Make widgets resizable by adding weight to the grid 
    for rows in range(1):
        XRD_submethods_frame.grid_rowconfigure(rows, weight=0)
        for columns in range(3):
            XRD_submethods_frame.grid_columnconfigure(columns, weight=1)
    
    #Call of 3rd-/widget-layer
    plot_widgetgrid = Fred_tkui_XRD_plot.widget_ui(mainwindow)
    rietveld_widgetgrid = Fred_tkui_XRD_rietveld.widget_ui(mainwindow)
    pdf_widgetgrid = Fred_tkui_XRD_pdf.widget_ui(mainwindow)
        
    #Visibility of 3rd- / widget-layer
    def plot():
        print('Pressed Plot')
        plot_widgetgrid.grid()
        rietveld_widgetgrid.grid_remove()
        pdf_widgetgrid.grid_remove()        
    def rietveld():
        print('Pressed Rietveld')
        plot_widgetgrid.grid_remove()
        rietveld_widgetgrid.grid()
        pdf_widgetgrid.grid_remove() 
    def pdf():
        print('Pressed PDF')
        plot_widgetgrid.grid_remove()
        rietveld_widgetgrid.grid_remove()
        pdf_widgetgrid.grid() 
    
    
      
    
    
    #Create of Buttonwidgets
    Button_XRD_plot = Button(XRD_submethods_frame, text='Plot', width=20, height = 1, state = "normal", command = plot)
    Button_XRD_rietveld = Button(XRD_submethods_frame, text='Rietveld', width=20, height = 1, state = "normal", command = rietveld)
    Button_XRD_pdf = Button(XRD_submethods_frame, text='PDF', width=20, height = 1, state = "normal", command = pdf)
    
    
    #Show in UI
    Button_XRD_plot.grid(row=0,column=0,sticky=N+S+E+W)
    Button_XRD_rietveld.grid(row=0,column=1,sticky=N+S+E+W)
    Button_XRD_pdf.grid(row=0,column=2,sticky=N+S+E+W) 
    
    
    #Make submenu_ui grid invisible
    #Return all grids including subgrids to be able to change visibility in 1st layer
    XRD_submethods_frame.grid_remove()
    return XRD_submethods_frame, plot_widgetgrid, rietveld_widgetgrid, pdf_widgetgrid
    