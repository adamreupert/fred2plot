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
import codecs


#Code section ---------------------------------------------

#Different processing blocks
def rename_automatic():
    importpath = './RIETVELD/rawdata/'
    onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
    for f in onlyfiles:
        filecp = codecs.open(('{}{}'.format(importpath, f)), encoding = 'cp1252')
        loaded_file = np.loadtxt(filecp, skiprows=2)
        exportpath = './RIETVELD/' + str(f)
        os.mkdir(exportpath[:-4])
        exportpath = './RIETVELD/' + str(f[:-4]) + '/rename/'
        os.mkdir(exportpath[:-1])
        exportpath += '/'
        np.savetxt('{}{}.csv'.format(exportpath, os.path.splitext(f)[0]), loaded_file, delimiter = ';')
    
    
def normalization_automatic():
    importpath = './RIETVELD/rawdata/'
    onlyfiles = [placeholder for placeholder in listdir(importpath) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:    
        importpath = './RIETVELD/' + str(placeholder[:-4]) + '/rename/'
        onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
        for f in onlyfiles:
            my_data = []
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            col = 0
            while(col < loaded_file.shape[1]):
                my_data.append(loaded_file[:,col])
                col = col+1
            my_data.append(loaded_file[:,1]/max(loaded_file[:,1]))
            my_data.append(loaded_file[:,2]/max(loaded_file[:,2]))
            my_data.append(loaded_file[:,5]/max(loaded_file[:,5]))
            result = np.array(my_data)
            result = result.T       
            exportpath = './RIETVELD/' + str(placeholder[:-4]) + '/normal/'
            os.mkdir(exportpath[:-1])
            exportpath += '/'
            np.savetxt('{}{}_normal.csv'.format(exportpath, os.path.splitext(f)[0]), result, delimiter = ';')
 
    
def plot_single_automatic_full():
    importpath = './RIETVELD/rawdata/'
    onlyfiles = [placeholder for placeholder in listdir(importpath) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:    
        importpath = './RIETVELD/' + str(placeholder[:-4]) + '/normal/'
        onlyfiles = [f for f in sorted(os.listdir(importpath)) if isfile(join(importpath, f))]
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[9:]
            f = f[:-11]
            plt.plot(loaded_file[:,0],loaded_file[:,6], 'ro', markerfacecolor='none', linewidth=0.5, label = 'Y$_{obs}$')
            plt.plot(loaded_file[:,0],loaded_file[:,7], 'k-', label = 'Y$_{calc}$')
            plt.plot(loaded_file[:,0],(loaded_file[:,6]-loaded_file[:,7])-0.5, 'b-', label = 'Y$_{obs-calc}$')
            plt.plot(loaded_file[:,4],(loaded_file[:,8]*0.0001)-0.25, 'g|', label = 'Bragg positions')
        plt.xlabel('2 Theta / [°]', fontsize = 15)
        plt.ylabel('Intensity / [a.u.]', fontsize = 15)
        plt.yticks([])
        plt.legend(loc='best', ncol=1)
        #plt.xlim(5,35)
        exportpath = './RIETVELD/' + str(placeholder[:-4]) + '/plot/'
        os.mkdir(exportpath[:-1])
        exportpath += '/'
        plt.savefig(exportpath + '01_RIETVELD_refinement.png', dpi=100, bbox_inches='tight')
        plt.clf()


def plot_single_automatic_cut():
    importpath = './RIETVELD/rawdata/'
    onlyfiles = [placeholder for placeholder in listdir(importpath) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:    
        importpath = './RIETVELD/' + str(placeholder[:-4]) + '/normal/'
        onlyfiles = [f for f in sorted(os.listdir(importpath)) if isfile(join(importpath, f))]
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[9:]
            f = f[:-11]
            plt.plot(loaded_file[:,0],loaded_file[:,6], 'ro', markerfacecolor='none', linewidth=0.5, label = 'Y$_{obs}$')
            plt.plot(loaded_file[:,0],loaded_file[:,7], 'k-', label = 'Y$_{calc}$')
            plt.plot(loaded_file[:,0],(loaded_file[:,6]-loaded_file[:,7])-0.5, 'b-', label = 'Y$_{obs-calc}$')
            plt.plot(loaded_file[:,4],(loaded_file[:,8]*0.0001)-0.25, 'g|', label = 'Bragg positions')
        plt.xlabel('2 Theta / [°]', fontsize = 15)
        plt.ylabel('Intensity / [a.u.]', fontsize = 15)
        plt.yticks([])
        plt.legend(loc='best', ncol=1)
        plt.xlim(3,35)
        exportpath = './RIETVELD/' + str(placeholder[:-4]) + '/plot/'
        os.mkdir(exportpath[:-1])
        exportpath += '/'
        plt.savefig(exportpath + '01_RIETVELD_refinement.png', dpi=100, bbox_inches='tight')
        plt.clf()