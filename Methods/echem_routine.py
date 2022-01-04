#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:50:50 2020

@author: Adam Reupert
"""

#Import section ------------------------------
import os
from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
import re
from tkinter import Tk
import tkinter.filedialog as fd
import pandas as pd

#Code section ---------------------------------------------

#Different processing blocks GCPL
def csv_convert():
    root2 = Tk()
    root2.withdraw() #use to hide tkinter window
    currdir = os.getcwd()
    impdir = fd.askdirectory(parent=root2, initialdir=currdir, title='Please select an import directory')
    if len(impdir) > 0:
        impdir = impdir + '/'
        print(impdir)
    currdir = os.getcwd()
    expdir = fd.askdirectory(parent=root2, initialdir=currdir, title='Please select an export directory')
    if len(expdir) > 0:
        expdir = expdir + '/'
        print(expdir)
    root2.destroy()
    importpath = impdir
    
    #read text file into pandas DataFrame
    onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
    for f in onlyfiles:
        
        readfile = '{}{}.mpt'.format(importpath, os.path.splitext(f)[0])
        fin = open(readfile, "rt")
        fout = open(readfile[:-4] + "_conv.txt", "wt")
        for line in fin:
            tab_replaced = line.replace('	', ';')
            commatab_replaced = tab_replaced.replace(',', '.')
            fout.write(commatab_replaced)
        fin.close()
        fout.close()
    onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
    for f in onlyfiles:
        if f.endswith("_conv.txt"):
            readfile = '{}{}.txt'.format(importpath, os.path.splitext(f)[0])
            for line in open(readfile):
                match = re.search('Nb header lines : (\d+)', line)
                if match:
                    headerlines = int(match.group(1))#-1 for 
                    print(headerlines)
            for line in open(readfile):
                match = re.search('Mass of active material : (\d+[.]?\d+)', line)
                if match:
                    activematerial = float(match.group(1))#-1 for 
                    #print(activematerial)
                    #activematerial[-3]
                    print('Activematerial: ' + str(activematerial))
            exportpath = expdir
            df = pd.read_table('{}{}'.format(importpath, f), skiprows= headerlines-1, encoding='cp1252', sep = ';')
            print(df.head(5))
            df.to_csv('{}{}.csv'.format(exportpath, os.path.splitext(f)[0]), decimal='.')
            os.remove('{}{}'.format(exportpath, f))
    print('Converted to .csv')
    csv_condensed(importpath,exportpath,activematerial)

def csv_condensed(importpath,exportpath,activematerial):
    onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
    for f in onlyfiles:
        if f.endswith("_conv.csv"):
            df = pd.read_csv("{}{}".format(importpath, f), header = 0,  sep =',', usecols = ['mode','time/s','Ecell/V','Q discharge/mA.h','Q charge/mA.h','cycle number'])
            print('Read:')
            for index in range(len(df['mode'])):
                if df['mode'][index] != 3:
                    OCVend = index
                    break
            i = 0
            while i < OCVend:
                df = df.drop(i)
                i += 1
            df.reset_index(drop=True, inplace=True)
            df.to_csv('{}{}_cond.csv'.format(exportpath, os.path.splitext(f)[0]), decimal='.')
    print('Condensed .csv file')
    #csv_cycle_plot(importpath,exportpath,activematerial)
    #csv_cycle_splitting(importpath,exportpath,activematerial)

def csv_capacity_plot():
    print('capacity plot')

def csv_cycle_splitting(importpath,exportpath,activematerial):
    onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
    for f in onlyfiles:
        if f.endswith("_cond.csv"):
            df = pd.read_csv("{}{}".format(importpath, f), header = 0,  sep =',', decimal='.', usecols = ['time/s','Ecell/V','Q discharge/mA.h','Q charge/mA.h','cycle number'])
            print('Read:')
            for index in range(len(df['Q charge/mA.h'])):
                if df['Q charge/mA.h'][index] != 0:
                    chargecycle = index
                    break
            dataframelength = df.shape[0]
            print(dataframelength)
            while chargecycle < dataframelength:
                df = df.drop(chargecycle)
                chargecycle += 1
            df.reset_index(drop=True, inplace=True)
            cycle = 1
            discharge = 1
            charge = 0
            if discharge == 1:
                discharge = 0
                charge = 1
                fileend = '_d' + str(cycle)
            if charge == 1:
                charge = 0   
                discharge = 1
                fileend = '_c' + str(cycle)
            df.to_csv('{}{}'.format(exportpath, os.path.splitext(f)[0]) + fileend + '.csv', decimal='.')
    print('Condensed .csv file')
            
    
    
    
    
    
def csv_cycle_plot(importpath,exportpath,activematerial):
    onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
    for f in onlyfiles:
        if f.endswith("_cond.csv"):
            df = pd.read_csv("{}{}".format(importpath, f), header = 0,  sep =',', decimal='.', usecols = ['time/s','Ecell/V','Q discharge/mA.h','Q charge/mA.h','cycle number'])
            print('Read:')
            #print(df.head(5))
            fig, (ax1) = plt.subplots(nrows= 1, ncols= 1, figsize=(4.8,4.8))
            cathodemass = 6.83
            activematerial = ((cathodemass-5.44)*0.7)/1000
            dataline = ax1.plot((df['Q discharge/mA.h']/activematerial),df['Ecell/V'],'-', linewidth = 0.6, label = f)
            dataline = ax1.plot((df['Q charge/mA.h']/activematerial),df['Ecell/V'],'-', linewidth = 0.6, label = f)
            #dataline = ax1.plot((df['cycle number']),df['Q discharge/mA.h']/activematerial,'-', linewidth = 0.6, label = f)
            #dataline = ax1.plot((df['cycle number']),df['Q charge/mA.h']/activematerial,'-', linewidth = 0.6, label = f)
            #dataline = ax1.plot((df['time/s']/3600),df['Ecell/V'],'-', linewidth = 0.6, label = f)
            dataline
            labeltext = f
            #ax1.set_xlim(3,70)
            #ax1.text((ax1.get_xlim()[1]-(ax1.get_xlim()[1]*0.025)), 0.5 + addition, labeltext, color= dataline[0].get_color(),ha = 'right')
            #addition = addition - 1.1
            ax1.set_xlabel('Q discharge / mA.h g-1')
            ax1.set_ylabel('Ecell vs Mg/Mg2+')
            #ax1.set(yticks=[])
            #ax1.text(-0.08, 0.97, string.ascii_uppercase[0]+')', transform=ax1.transAxes, size=15)
            #fig.subplots_adjust(hspace=0.25)
            plt.savefig('{}{}.svg'.format(exportpath, os.path.splitext(f)[0]), dpi=100, bbox_inches='tight')            
            
            
            
            # for index in range(len(df['mode'])):
            #     if df['mode'][index] != 3:
            #         OCVend = index
            #         break
            # i = 0
            # print(OCVend)
            # while i < OCVend:
            #     df = df.drop(i)
            #     i += 1
            # df.reset_index(drop=True, inplace=True)
            # df.to_csv('{}{}_condensed.csv'.format(exportpath, os.path.splitext(f)[0]), decimal='.')
    print('cycle plot')

def normalization_automatic_XRD():
    importpath = './0_xy/'
    onlyfiles = [placeholder for placeholder in listdir(importpath) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:    
        importpath = './' + str(placeholder[:-3]) + '/baseline/'
        onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
        for f in onlyfiles:
            my_data = []
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            col = 0
            while(col < loaded_file.shape[1]):
                my_data.append(loaded_file[:,col])
                col = col+1
            my_data.append(loaded_file[:,1]/max(loaded_file[:,1]))
            my_data.append(loaded_file[:,3]/max(loaded_file[:,3]))
            result = np.array(my_data)
            result = result.T       
            exportpath = './' + str(placeholder[:-3]) + '/normal/'
            os.mkdir(exportpath[:-1])
            exportpath += '/'
            np.savetxt('{}{}_normal.csv'.format(exportpath, os.path.splitext(f)[0]), result, delimiter = ';')



#Plotting of a 2x2 grid with all four graphs
def plot():
    importpath = './0_xy/'
    onlyfiles = [placeholder for placeholder in sorted(os.listdir(importpath)) if isfile(join(importpath, placeholder))]
    addition = 0
    fig, (ax1) = plt.subplots(nrows= 1, ncols= 1, figsize=(4.8,4.8))
    for placeholder in onlyfiles:    
        importpath = './' + str(placeholder[:-3]) + '/normal/'
        onlyfiles = [f for f in sorted(os.listdir(importpath)) if isfile(join(importpath, f))]
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[:-27]
            dataline = ax1.plot(loaded_file[:,0],(loaded_file[:,5]+addition),'-', linewidth = 0.6, label = f)
            dataline
            labeltext = f
            #ax1.set_xlim(3,70)
            ax1.text((ax1.get_xlim()[1]-(ax1.get_xlim()[1]*0.025)), 0.5 + addition, labeltext, color= dataline[0].get_color(),ha = 'right')
            addition = addition - 1.1
            ax1.set_xlabel('2 Theta / [°]')
            ax1.set_ylabel('Intensity / [a.u.]')
            ax1.set(yticks=[])
            #ax1.text(-0.08, 0.97, string.ascii_uppercase[0]+')', transform=ax1.transAxes, size=15)
    fig.subplots_adjust(hspace=0.25)
    exportpath = './'  
    plt.savefig(exportpath + 'VS4_001_001_001_XRD_uncut.svg', dpi=100, bbox_inches='tight')
    importpath = './0_xy/'
    onlyfiles = [placeholder for placeholder in sorted(os.listdir(importpath)) if isfile(join(importpath, placeholder))]
    addition = 0
    fig, (ax1) = plt.subplots(nrows= 1, ncols= 1, figsize=(4.8,4.8))
    for placeholder in onlyfiles:    
        importpath = './' + str(placeholder[:-3]) + '/normal/'
        onlyfiles = [f for f in sorted(os.listdir(importpath)) if isfile(join(importpath, f))]
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[:-27]
            dataline = ax1.plot(loaded_file[:,0],(loaded_file[:,5]+addition),'-', linewidth = 0.6, label = f)
            dataline
            labeltext = f
            ax1.set_xlim(5,40)
            ax1.text((ax1.get_xlim()[1]-(ax1.get_xlim()[1]*0.025)), 0.5 + addition, labeltext, color= dataline[0].get_color(),ha = 'right')
            addition = addition - 1.1
            ax1.set_xlabel('2 Theta / [°]')
            ax1.set_ylabel('Intensity / [a.u.]')
            ax1.set(yticks=[])
            #ax1.text(-0.08, 0.97, string.ascii_uppercase[0]+')', transform=ax1.transAxes, size=15)
    fig.subplots_adjust(hspace=0.25)
    exportpath = './'  
    plt.savefig(exportpath + 'VS4_001_001_001_XRD_cut.svg', dpi=100, bbox_inches='tight')

def run():
    csv_convert()
   #csv_condensed() 
   #csv_capacity_plot()
   #csv_cycle_plot()
   #normalization_automatic_XRD()
   #plot()

#Call restriction for other scripts & when used directly -------
if __name__ == "__main__":
    run()
    

