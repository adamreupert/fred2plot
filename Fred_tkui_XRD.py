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

def menus(mainwindow):    
    
    #Creation of 3rd- / widget-layer
    plot_widgetgrid = Fred_tkui_XRD_plot.widgetui(mainwindow)
    rietveld_widgetgrid = Fred_tkui_XRD_rietveld.widgetui(mainwindow)
    pdf_widgetgrid = Fred_tkui_XRD_pdf.widgetui(mainwindow)
        
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
    
    
    
    
    #Creation of 2nd layer / submenu grid and buttons (Plot,Rietveld,...) & hide when first initialized
    XRD_submethods_frame=Frame(mainwindow)
    XRD_submethods_frame.grid(row=2, column=0, columnspan=3) # Columnspan has to be the same number as there are submenus    
    Button_XRD_plot = Button(XRD_submethods_frame, text='Plot', width=25, height = 1, state = "normal", command = plot)
    Button_XRD_plot.grid(row=0,column=0,sticky=N+S)
    Button_XRD_rietveld = Button(XRD_submethods_frame, text='Rietveld', width=25, height = 1, state = "normal", command = rietveld)
    Button_XRD_rietveld.grid(row=0,column=1,sticky=N+S)
    Button_XRD_pdf = Button(XRD_submethods_frame, text='PDF', width=25, height = 1, state = "normal", command = pdf)
    Button_XRD_pdf.grid(row=0,column=2,sticky=N+S)
    XRD_submethods_frame.grid_remove()
    
    
    # Return of 2nd layer subgrid to be callable from Fred_tkui class
    return XRD_submethods_frame
    









# def menus(mainwindow):
    
#     def xrd_plot():
#         XRD_plotmenu_frame.grid()

    
#     # Creation of subgrids
#     XRD_submethods_frame=Frame(mainwindow)
#     XRD_submethods_frame.grid(row=2, column=0, columnspan=3) # Columnspan has to be the same number as there are submenus
#     XRD_plotmenu_frame=Frame(mainwindow)
#     XRD_plotmenu_frame.grid(row=4, column=0, columnspan=7) # Columnspan has to be the same number as there are in total

#     #Creation of first subgrid (Plot,Rietveld,...) & hide when first initialized
#     Button_XRD_rietveld = Button(XRD_submethods_frame, text='Rietveld', width=25, height = 1, state = "normal")
#     Button_XRD_rietveld.grid(row=0,column=1,sticky=N+S)
#     Button_XRD_pdf = Button(XRD_submethods_frame, text='PDF', width=25, height = 1, state = "normal")
#     Button_XRD_pdf.grid(row=0,column=2,sticky=N+S)
#     Button_XRD_plot = Button(XRD_submethods_frame, text='Plot', width=25, height = 1, state = "normal", command = xrd_plot)
#     Button_XRD_plot.grid(row=0,column=0,sticky=N+S)
#     XRD_submethods_frame.grid_remove()
    
#     #Creation of Plot widget & hide when first initialized
#     Button_XRD_plot_widget = Button(XRD_plotmenu_frame, text='Generate', width=25, height = 1, state = "normal")
#     Button_XRD_plot_widget.grid(row=0,column=0,sticky=N+S)
#     XRD_plotmenu_frame.grid_remove()
    
#     # Return of first subgrid to be callable from Fred_tkui class
#     return XRD_submethods_frame
    
    