# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:19:54 2022

@author: Adam_Reupert
"""

#Import the required libraries
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def widget_ui(mainwindow):
    
    #Create of 3rd-layer grid for the Plot widgets
    widgetgrid = Frame(mainwindow)
    widgetgrid.grid(row=4, column=0, columnspan=7) # Columnspan has to be the same number as there are in total
    
    
    #Create of widgets
    
    Label_Titeltext = Label(widgetgrid, text= "    XRD-Menu    ", font=('Helvetica bold',20))
    
    
    ###############    Graph    ###############
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5), dpi = 100)  
    # list of squares
    y = [-i**2 for i in range(101)]
    # adding the subplot
    plot1 = fig.add_subplot(111)
    # plotting the graph
    plot1.plot(y)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = widgetgrid)     
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row=2, column=0, sticky=N+S+E+W)
    # creating the Matplotlib toolbar
    ###############    TOOLBAR    ###############
    toolbarFrame = Frame(master=widgetgrid)
    toolbarFrame.grid(row=3,column=0)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
    
    Button_XRD_plot_widget = Button(widgetgrid, text='Plot', width=25, height = 1, state = "normal")    
    
    #Label
    #Label_plotformat_XRD = Label(XRD_frame, text='Which kind of plot do you want?')
        
    # #RadioButtons
    # plotformat = IntVar()
    # plotformat.set(1)
    # Radiobutton_plotformat_XRD1 = Radiobutton(XRD_frame, text='Single-plot', variable=plotformat, value=1)
    # Radiobutton_plotformat_XRD2 = Radiobutton(XRD_frame, text='Multi-plot', variable=plotformat, value=2) 
    # Radiobutton_plotformat_XRD3 = Radiobutton(XRD_frame, text='Rietveld-plot', variable=plotformat, value=3) 
      
    # #Data processing options
    # Label_option_XRD = Label(XRD_frame, text='Data processing options:')
    # option_rename = IntVar()
    # option_rename.set(1)
    # Checkbox_option_rename_XRD = Checkbutton(XRD_frame, text="File reformatting", variable=option_rename)
    # option_baseline = IntVar()
    # option_baseline.set(1)
    # Checkbox_option_baseline_XRD = Checkbutton(XRD_frame, text="Baseline substraction", variable=option_baseline, command=update_baseline_entry_plotoptions)
    # option_norm = IntVar()
    # option_norm.set(1)
    # Checkbox_option_norm_XRD = Checkbutton(XRD_frame, text="Normalization", variable=option_norm)
    # option_fileexp = IntVar()
    # option_fileexp.set(1)
    # Checkbox_option_fileexp_XRD = Checkbutton(XRD_frame, text="Export results as csv file", variable=option_fileexp)
    # option_svgexp = IntVar()
    # option_svgexp.set(1)
    # Checkbox_option_svgexp_XRD = Checkbutton(XRD_frame, text="SVG image export", variable=option_svgexp)
    # option_pngexp = IntVar()
    # option_pngexp.set(0)
    # Checkbox_option_pngexp_XRD = Checkbutton(XRD_frame, text="PNG image export", variable=option_pngexp)
    
    #Show in UI
    Label_Titeltext.grid(row=0,column=4,sticky=N+S+E+W)
    widgetgrid.grid_rowconfigure(1, minsize=10)
    Button_XRD_plot_widget.grid(row=4,column=0,sticky=N+S)
    #Plotcanvas_XRD.get_tk_widget().grid(row=2, column=0, sticky=N+S+E+W)
    
    
    
    
    
    #Make widget_ui grid invisible
    #Return grid to be able to change visibility in upper layers
    widgetgrid.grid_remove()
    return widgetgrid

# #Functions for XRD menu

# def update_baseline_entry_plotoptions():
#     if option_baseline.get() == 1:
#         Entry_plotoptions_baselambda_XRD['state'] = 'normal'
#         Entry_plotoptions_baseasym_XRD['state'] = 'normal'
#     if option_baseline.get() == 0:
#         Entry_plotoptions_baselambda_XRD['state'] = 'disabled'
#         Entry_plotoptions_baseasym_XRD['state'] = 'disabled'

# def XRD_load():
#     print('Load')
#     XRD_import_window = Tk()
#     XRD_import_window.withdraw() #use to hide tkinter window
#     currdir = os.getcwd()
#     impdir = fd.askdirectory(parent=XRD_import_window, initialdir=currdir, title='Please select a import directory')
#     if len(impdir) > 0:
#         impdir = impdir + '/'
#         print(impdir)
#         XRD_load.variable = impdir
#     XRD_import_window.destroy()
#     Label_inputdir_result_XRD['text'] = impdir
    
# def XRD_export():
#     print('Export')
#     XRD_export_window = Tk()
#     XRD_export_window.withdraw()
#     currdir = os.getcwd()
#     expdir = fd.askdirectory(parent=XRD_export_window, initialdir=currdir, title='Please select a export directory')
#     if len(expdir) > 0:
#         expdir = expdir + '/'
#         print(expdir)
#         XRD_export.variable = expdir    
#     XRD_export_window.destroy()
#     Label_exportdir_result_XRD['text'] = expdir

# def XRD_generate():
#     if Label_inputdir_result_XRD['text'] == 'Nothing selected':
#         print('You did not specify import directory')
#     elif Label_exportdir_result_XRD['text'] == 'Nothing selected':
#         print('You did not specify export directory')
#     else:
#         print('Fire in the hole!')    
#         if option_rename.get():
#             print("File is reformated")
#             Fred_xrd_routine.rename_automatic_XRD(XRD_load.variable, XRD_export.variable)
#         if option_baseline.get():
#             print("File is baseline substracted")
#             #Fred_xrd_routine.baseline_substraction_automatic_XRD()
#         if option_norm.get():
#             print("File is normalized") 
#             #Fred_xrd_routine.normalization_automatic_XRD()
#         if option_svgexp.get():
#             print("Image is exported as SVG")
#             #Fred_xrd_routine.plot()
#         if option_pngexp.get():
#             print("Image is exported as PNG") 
#             #Fred_xrd_routine.plot()


    
# # Options for shaping the plot
# Label_plotoptions_XRD = Label(XRD_frame, text='Plot options:')
# Label_plotoptions_baselambda_XRD = Label(XRD_frame, text='λ (10^2 to 10^9)')
# Entry_plotoptions_baselambda_XRD = Entry(XRD_frame)
# Entry_plotoptions_baselambda_XRD.insert(0, '1000000')
# Label_plotoptions_baseasym_XRD = Label(XRD_frame, text='Asym. (10e-3 to 10e-1)')
# Entry_plotoptions_baseasym_XRD = Entry(XRD_frame)
# Entry_plotoptions_baseasym_XRD.insert(0, '0.001')
# update_baseline_entry_plotoptions()
# Label_plotoptions_x1_XRD = Label(XRD_frame, text='Start X')
# Entry_plotoptions_x1_XRD = Entry(XRD_frame)
# Entry_plotoptions_x1_XRD.insert(0, '0')
# Label_plotoptions_x2_XRD = Label(XRD_frame, text='End X')
# Entry_plotoptions_x2_XRD = Entry(XRD_frame)
# Entry_plotoptions_x2_XRD.insert(0, '60')
# Label_plotoptions_y1_XRD = Label(XRD_frame, text='Start Y')
# Entry_plotoptions_y1_XRD = Entry(XRD_frame)
# Entry_plotoptions_y1_XRD.insert(0, '0')
# Label_plotoptions_y2_XRD = Label(XRD_frame, text='End Y')
# Entry_plotoptions_y2_XRD = Entry(XRD_frame)
# Entry_plotoptions_y2_XRD.insert(0, '1.5')
    
# #Import und export directory
# Button_inputdir_XRD = Button(XRD_frame, text='Load', width=15, height = 1, state = "normal", command = XRD_load)
# Button_exportdir_XRD = Button(XRD_frame, text='Export', width=15, height = 1, state = "normal", command = XRD_export)
# Label_inputdir_XRD = Label(XRD_frame, text='Input-Dir:')
# Label_exportdir_XRD = Label(XRD_frame, text='Export-Dir:')
# Label_inputdir_result_XRD = Label(XRD_frame, text='Nothing selected')
# Label_exportdir_result_XRD = Label(XRD_frame, text='Nothing selected')
    
# #Generate Button
# Button_generate_XRD = Button(XRD_frame, text='Generate', width=15, height = 1, state = "normal", command = XRD_generate)

# #Shoving into screen using grid system
# #XRD-Menu and its widgets
# Label_header_XRD.grid(row=0,column=0, columnspan=24, sticky=N+S+E+W)
# Plotcanvas_XRD.get_tk_widget().grid(row=1, column=0, rowspan = 24, columnspan=15, sticky=N+S+E+W)
# Label_plotformat_XRD.grid(row=1,column=15, columnspan=9, sticky=N+S+W)
# Radiobutton_plotformat_XRD1.grid(row=2,column=16,columnspan=2, sticky=N+S+E+W)
# Radiobutton_plotformat_XRD2.grid(row=2,column=19,columnspan=2, sticky=N+S+E+W)
# Radiobutton_plotformat_XRD3.grid(row=2,column=22,columnspan=2, sticky=N+S+E+W)
# Label_option_XRD.grid(row=3,column=15, columnspan=9, sticky=N+S+W)
# Checkbox_option_rename_XRD.grid(row=4,column=16,columnspan=4, sticky=N+S+W)
# Checkbox_option_baseline_XRD.grid(row=4,column=20,columnspan=4, sticky=N+S+W)
# Checkbox_option_norm_XRD.grid(row=5,column=16,columnspan=4, sticky=N+S+W)
# Checkbox_option_fileexp_XRD.grid(row=5,column=20,columnspan=4, sticky=N+S+W)
# Checkbox_option_pngexp_XRD.grid(row=6,column=16,columnspan=4, sticky=N+S+W)
# Checkbox_option_svgexp_XRD.grid(row=6,column=20,columnspan=4, sticky=N+S+W)
# Label_plotoptions_XRD.grid(row=7,column=15, columnspan=9, sticky=N+S+W)
    
# Label_plotoptions_baselambda_XRD.grid(row=8,column=16,columnspan=2, sticky=N+S+W)
# Entry_plotoptions_baselambda_XRD.grid(row=8,column=18,columnspan=2, sticky=N+S+W)
# Label_plotoptions_baseasym_XRD.grid(row=8,column=20,columnspan=2, sticky=N+S+W)
# Entry_plotoptions_baseasym_XRD.grid(row=8,column=22,columnspan=2, sticky=N+S+W)
    
# Label_plotoptions_x1_XRD.grid(row=9,column=16,columnspan=2, sticky=N+S+W)
# Entry_plotoptions_x1_XRD.grid(row=9,column=18,columnspan=2, sticky=N+S+W)
# Label_plotoptions_x2_XRD.grid(row=9,column=20,columnspan=2, sticky=N+S+W)
# Entry_plotoptions_x2_XRD.grid(row=9,column=22,columnspan=2, sticky=N+S+W)
# Label_plotoptions_y1_XRD.grid(row=10,column=16,columnspan=2, sticky=N+S+W)
# Entry_plotoptions_y1_XRD.grid(row=10,column=18,columnspan=2, sticky=N+S+W)
# Label_plotoptions_y2_XRD.grid(row=10,column=20,columnspan=2, sticky=N+S+W)
# Entry_plotoptions_y2_XRD.grid(row=10,column=22,columnspan=2, sticky=N+S+W)
    
    
    
    
    
    
    
    
    
    
    
# Button_inputdir_XRD.grid(row=20,column=16,columnspan=4, sticky=N+S+E+W)
# Button_exportdir_XRD.grid(row=20,column=20,columnspan=4, sticky=N+S+E+W)
# Label_inputdir_XRD.grid(row=21,column=16,columnspan=2, sticky=N+S+W)
# Label_exportdir_XRD.grid(row=22,column=16,columnspan=2, sticky=N+S+W)
# Label_inputdir_result_XRD.grid(row=21,column=18,columnspan=3, sticky=N+S+W)
# Label_exportdir_result_XRD.grid(row=22,column=18,columnspan=3, sticky=N+S+W)

# Button_generate_XRD.grid(row=23,column=15,columnspan=9, sticky=N+S+E+W)