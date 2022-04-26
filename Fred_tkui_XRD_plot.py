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
    widgetgrid.grid(row=2, column=0, columnspan = 8, sticky=N+S+E+W) # Columnspan has to be the same number as there are in total
    
    #Create of widgets
    #Title
    Label_Titeltext = Label(widgetgrid, text= "XRD-Menu", font=('Helvetica 20 bold underline'))
    
#Left UI side
    #BG Label
    Label_leftBG = Label(widgetgrid, bg = "#a8a8a8")
    # Graph
    fig = Figure(figsize = (4, 4), dpi = 100)  
    y = [-i for i in range(101)]
    plot1 = fig.add_subplot(111)
    plot1.plot(y)

    canvas = FigureCanvasTkAgg(fig, master = widgetgrid)     
    canvas.draw()
    toolbarFrame = Frame(master=widgetgrid)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
    
#Right UI side
    Label_rightBG = Label(widgetgrid, bg = "#a8a8a8")
    
    #Plot format
    Label_plotformat = Label(widgetgrid, text= "Plot-format:", font=('Helvetica 10 underline'))
    formatchoice = IntVar()
    formatchoice.set(1)
    Radiobutton_plotformat_single = Radiobutton(widgetgrid, text='Single-plot', variable=formatchoice, value=1)
    Radiobutton_plotformat_multi = Radiobutton(widgetgrid, text='Multi-plot', variable=formatchoice, value=2) 
    #Data processing options   
    Label_plot_processing = Label(widgetgrid, text= "Data processing options:", font=('Helvetica 10 underline'))  
    option_rename = IntVar()
    option_rename.set(1)
    Checkbox_option_rename = Checkbutton(widgetgrid, text="File reformatting", variable=option_rename)
    option_baseline = IntVar()
    option_baseline.set(1)
    Checkbox_option_baseline = Checkbutton(widgetgrid, text="Baseline substraction", variable=option_baseline)#, command=update_baseline_entry_plotoptions)
    option_norm = IntVar()
    option_norm.set(1)
    Checkbox_option_norm = Checkbutton(widgetgrid, text="Normalization", variable=option_norm)
    option_fileexp = IntVar()
    option_fileexp.set(1)
    Checkbox_option_fileexp = Checkbutton(widgetgrid, text="Export results as csv file", variable=option_fileexp)
    option_svgexp = IntVar()
    option_svgexp.set(1)
    Checkbox_option_svgexp = Checkbutton(widgetgrid, text="SVG image export", variable=option_svgexp)
    option_pngexp = IntVar()
    option_pngexp.set(0)
    Checkbox_option_pngexp = Checkbutton(widgetgrid, text="PNG image export", variable=option_pngexp) 
    # # Options for shaping the plot
    Label_plotoptions = Label(widgetgrid, text= "Plot options:", font=('Helvetica 10 underline'))
    Label_plotoptions_baselambda = Label(widgetgrid, text='Smoothing λ')
    Entry_plotoptions_baselambda = Entry(widgetgrid)
    Label_plotoptions_baselambda_hint = Label(widgetgrid, text='(10^2 to 10^9)')
    Entry_plotoptions_baselambda.insert(0, '1000000')
    Label_plotoptions_baseasym = Label(widgetgrid, text='Asymmetry')
    Entry_plotoptions_baseasym = Entry(widgetgrid)
    Label_plotoptions_baseasym_hint = Label(widgetgrid, text='(10e-1 to 10e-3)')
    Entry_plotoptions_baseasym.insert(0, '0.001')
    #update_baseline_entry_plotoptions()
    Label_plotoptions_x1 = Label(widgetgrid, text='Start X')
    Entry_plotoptions_x1 = Entry(widgetgrid)
    Entry_plotoptions_x1.insert(0, '0')
    Label_plotoptions_x2 = Label(widgetgrid, text='End X')
    Entry_plotoptions_x2 = Entry(widgetgrid)
    Entry_plotoptions_x2.insert(0, '60')
    Label_plotoptions_y1 = Label(widgetgrid, text='Start Y')
    Entry_plotoptions_y1 = Entry(widgetgrid)
    Entry_plotoptions_y1.insert(0, '0')
    Label_plotoptions_y2 = Label(widgetgrid, text='End Y')
    Entry_plotoptions_y2 = Entry(widgetgrid)
    Entry_plotoptions_y2.insert(0, '1.5')
    #Import und export directory
    Button_inputdir = Button(widgetgrid, text='Load', state = "normal")#, command = XRD_load)
    Button_exportdir = Button(widgetgrid, text='Export', state = "normal")#, command = XRD_export)
    Label_inputdir = Label(widgetgrid, text='Dir:')
    Label_exportdir = Label(widgetgrid, text='Dir:')
    Label_inputdir_result = Label(widgetgrid, text='Nothing selected')
    Label_exportdir_result = Label(widgetgrid, text='Nothing selected')    
    # #Generate/Update Button
    Button_generate = Button(widgetgrid, text='Generate & update plot', state = "normal")#, command = XRD_generate)
#Center UI side
    
    

#Show in UI
    
    #Rough size configurations of columns
    widgetgrid.grid_columnconfigure(0, minsize=15)
    
    widgetgrid.grid_columnconfigure(1, minsize=50)
    widgetgrid.grid_columnconfigure(2, minsize=50)
    widgetgrid.grid_columnconfigure(3, minsize=50)
    widgetgrid.grid_columnconfigure(4, minsize=50)
    widgetgrid.grid_columnconfigure(5, minsize=50)
    widgetgrid.grid_columnconfigure(6, minsize=50)
    widgetgrid.grid_columnconfigure(7, minsize=50)
    widgetgrid.grid_columnconfigure(8, minsize=50)
    widgetgrid.grid_columnconfigure(9, minsize=50)
    widgetgrid.grid_columnconfigure(10, minsize=50)
    widgetgrid.grid_columnconfigure(11, minsize=50)
    widgetgrid.grid_columnconfigure(12, minsize=50)

    widgetgrid.grid_columnconfigure(13, minsize=49)

    widgetgrid.grid_columnconfigure(14, minsize=50)
    widgetgrid.grid_columnconfigure(15, minsize=50)
    widgetgrid.grid_columnconfigure(16, minsize=50)
    widgetgrid.grid_columnconfigure(17, minsize=50)
    widgetgrid.grid_columnconfigure(18, minsize=50)
    widgetgrid.grid_columnconfigure(19, minsize=50)
    widgetgrid.grid_columnconfigure(20, minsize=50)
    widgetgrid.grid_columnconfigure(21, minsize=50)
    widgetgrid.grid_columnconfigure(22, minsize=50)
    widgetgrid.grid_columnconfigure(23, minsize=50)
    widgetgrid.grid_columnconfigure(24, minsize=50)
    widgetgrid.grid_columnconfigure(25, minsize=50)
    
    widgetgrid.grid_columnconfigure(26, minsize=15)
    
    for xcol in range(27):
         for xrow in range(30):
            if xrow % 2 !=0:
                if xcol % 2 !=0:
                    Label_right = Label(widgetgrid, bg = "#a8a8a8")
                    Label_right.grid(row=0,column=xcol, sticky=N+S+W+E) #You have to change 0 with xrows for chessboard structure
                else:
                    Label_right = Label(widgetgrid, bg = "#a1a1a1")
                    Label_right.grid(row=0,column=xcol, sticky=N+S+W+E)
            # else:
            #     if xcol % 2 !=0:
            #         Label_right = Label(widgetgrid, bg = "#a1a1a1")
            #         Label_right.grid(row=xrow,column=xcol, sticky=N+S+W+E)
            #     else:
            #         Label_right = Label(widgetgrid, bg = "#a8a8a8")
            #         Label_right.grid(row=xrow,column=xcol, sticky=N+S+W+E)
                
    
    
    
    widgetgrid.grid_rowconfigure(0, minsize=10)
    Label_Titeltext.grid(row=1,column=12, columnspan=3, sticky=N+S+E+W)
    widgetgrid.grid_rowconfigure(2, minsize=10)
    widgetgrid.grid_rowconfigure(3, minsize=20)
#Left side
    Label_leftBG.grid(row=3,column=1, columnspan=12, rowspan=24, sticky=N+S+E+W)
    canvas.get_tk_widget().grid(row=4, column=2, rowspan=20, columnspan=10)
    toolbarFrame.grid(row=24,column=3, columnspan=8, sticky=N+S+E+W)
#Right side
    #Label_rightBG.grid(row=3,column=14, columnspan=12, rowspan=24, sticky=N+S+W+E)
    Label_plotformat.grid(row=4,column=15, columnspan = 10, sticky=N+S+W)
    Radiobutton_plotformat_single.grid(row=5,column=15,columnspan=2, sticky=N+S+E+W)
    Radiobutton_plotformat_multi.grid(row=5,column=17,columnspan=2, sticky=N+S+E+W)
    Label_plot_processing.grid(row=6,column=15, columnspan = 10, sticky=N+S+W)
    Checkbox_option_rename.grid(row=7,column=15,columnspan=3, sticky=N+S+W)
    Checkbox_option_baseline.grid(row=7,column=18,columnspan=4, sticky=N+S+W)
    Checkbox_option_norm.grid(row=8,column=15,columnspan=3, sticky=N+S+W)
    Checkbox_option_fileexp.grid(row=8,column=18,columnspan=4, sticky=N+S+W)
    Checkbox_option_pngexp.grid(row=9,column=15,columnspan=3, sticky=N+S+W)
    Checkbox_option_svgexp.grid(row=9,column=18,columnspan=4, sticky=N+S+W)
    Label_plotoptions.grid(row=10,column=15, columnspan=10, sticky=N+S+W)
    Label_plotoptions_baselambda.grid(row=11,column=15,columnspan=2, sticky=N+S+W)
    Entry_plotoptions_baselambda.grid(row=11,column=17,columnspan=3, sticky=N+S+W)
    Label_plotoptions_baselambda_hint.grid(row=11,column=20,columnspan=2, sticky=N+S+W)
    Label_plotoptions_baseasym.grid(row=12,column=15,columnspan=2, sticky=N+S+W)
    Entry_plotoptions_baseasym.grid(row=12,column=17,columnspan=3, sticky=N+S+W)
    Label_plotoptions_baseasym_hint.grid(row=12,column=20,columnspan=2, sticky=N+S+W)    
    Label_plotoptions_x1.grid(row=13,column=15,columnspan=2, sticky=N+S+W)
    Entry_plotoptions_x1.grid(row=13,column=17,columnspan=3, sticky=N+S+W)
    Label_plotoptions_x2.grid(row=13,column=20,columnspan=2, sticky=N+S+W)
    Entry_plotoptions_x2.grid(row=13,column=22,columnspan=3, sticky=N+S+W)
    Label_plotoptions_y1.grid(row=14,column=15,columnspan=2, sticky=N+S+W)
    Entry_plotoptions_y1.grid(row=14,column=17,columnspan=3, sticky=N+S+W)
    Label_plotoptions_y2.grid(row=14,column=20,columnspan=2, sticky=N+S+W)
    Entry_plotoptions_y2.grid(row=14,column=22,columnspan=3, sticky=N+S+W)
    Button_inputdir.grid(row=15,column=15, columnspan=2, sticky=N+S+W+E)
    Button_exportdir.grid(row=16,column=15, columnspan=2, sticky=N+S+W+E)
    Label_inputdir.grid(row=15,column=17, columnspan=1, sticky=N+S+E+W)
    Label_exportdir.grid(row=16,column=17, columnspan=1, sticky=N+S+E+W)
    Label_inputdir_result.grid(row=15,column=18, columnspan=5, sticky=N+S+W)
    Label_exportdir_result.grid(row=16,column=18, columnspan=5, sticky=N+S+W)
    widgetgrid.grid_rowconfigure(17, minsize=10)
    Button_generate.grid(row=18,column=15, columnspan=10, sticky=N+S+W+E)
    
    
    
#Center side
    widgetgrid.grid_rowconfigure(26, minsize=20)
    widgetgrid.grid_rowconfigure(27, minsize=20)
    
    
    #Make widget_ui grid invisible
    #Return grid to be able to change visibility in upper layers
    widgetgrid.grid_remove()
    return widgetgrid






    
    
    
    
    
    
    
    
    
    
    
# Button_inputdir.grid(row=20,column=16,columnspan=4, sticky=N+S+E+W)
# Button_exportdir.grid(row=20,column=20,columnspan=4, sticky=N+S+E+W)
# Label_inputdir.grid(row=21,column=16,columnspan=2, sticky=N+S+W)
# Label_exportdir.grid(row=22,column=16,columnspan=2, sticky=N+S+W)
# Label_inputdir_result.grid(row=21,column=18,columnspan=3, sticky=N+S+W)
# Label_exportdir_result.grid(row=22,column=18,columnspan=3, sticky=N+S+W)

# Button_generate.grid(row=23,column=15,columnspan=9, sticky=N+S+E+W)









# #Functions for XRD menu

# def update_baseline_entry_plotoptions():
#     if option_baseline.get() == 1:
#         Entry_plotoptions_baselambda['state'] = 'normal'
#         Entry_plotoptions_baseasym['state'] = 'normal'
#     if option_baseline.get() == 0:
#         Entry_plotoptions_baselambda['state'] = 'disabled'
#         Entry_plotoptions_baseasym['state'] = 'disabled'

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
#     Label_inputdir_result['text'] = impdir
    
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
#     Label_exportdir_result['text'] = expdir

# def XRD_generate():
#     if Label_inputdir_result['text'] == 'Nothing selected':
#         print('You did not specify import directory')
#     elif Label_exportdir_result['text'] == 'Nothing selected':
#         print('You did not specify export directory')
#     else:
#         print('Fire in the hole!')    
#         if option_rename.get():
#             print("File is reformated")
#             Fred_routine.rename_automatic(XRD_load.variable, XRD_export.variable)
#         if option_baseline.get():
#             print("File is baseline substracted")
#             #Fred_routine.baseline_substraction_automatic()
#         if option_norm.get():
#             print("File is normalized") 
#             #Fred_routine.normalization_automatic()
#         if option_svgexp.get():
#             print("Image is exported as SVG")
#             #Fred_routine.plot()
#         if option_pngexp.get():
#             print("Image is exported as PNG") 
#             #Fred_routine.plot()