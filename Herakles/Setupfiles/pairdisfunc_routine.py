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
    importpath = './PDF/rawdata/'
    onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
    for f in onlyfiles:
        filecp = codecs.open(('{}{}'.format(importpath, f)), encoding = 'cp1252')
        loaded_file = np.loadtxt(filecp, skiprows=27)
        exportpath = './PDF/' + str(f)
        os.mkdir(exportpath[:-4])
        exportpath = './PDF/' + str(f[:-4]) + '/rename/'
        os.mkdir(exportpath[:-1])
        exportpath += '/'
        np.savetxt('{}{}.csv'.format(exportpath, os.path.splitext(f)[0]), loaded_file, delimiter = ';')
    
    
def normalization_automatic():
    importpath = './PDF/rawdata/'
    onlyfiles = [placeholder for placeholder in listdir(importpath) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:    
        importpath = './PDF/' + str(placeholder[:-4]) + '/rename/'
        onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
        for f in onlyfiles:
            my_data = []
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            col = 0
            while(col < loaded_file.shape[1]):
                my_data.append(loaded_file[:,col])
                col = col+1
            my_data.append(loaded_file[:,1]/max(loaded_file[:,1]))
            result = np.array(my_data)
            result = result.T       
            exportpath = './PDF/' + str(placeholder[:-4]) + '/normal/'
            os.mkdir(exportpath[:-1])
            exportpath += '/'
            np.savetxt('{}{}_normal.csv'.format(exportpath, os.path.splitext(f)[0]), result, delimiter = ';')
 
    
def plot_single_automatic():
    importpath = './PDF/rawdata/'
    onlyfiles = [placeholder for placeholder in listdir(importpath) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:    
        importpath = './PDF/' + str(placeholder[:-4]) + '/normal/'
        onlyfiles = [f for f in sorted(os.listdir(importpath)) if isfile(join(importpath, f))]
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[16:]
            f = f[:-30]
            plt.plot(loaded_file[:,0],loaded_file[:,2], '-', label = f)
        plt.xlabel('r / [Å]', fontsize = 15)
        plt.ylabel('G(r)', fontsize = 15)
        plt.yticks([])
        plt.legend(loc='best', ncol=1)
        exportpath = './PDF/' + str(placeholder[:-4]) + '/plot/'
        os.mkdir(exportpath[:-1])
        exportpath += '/'
        plt.savefig(exportpath + '01_PDF_full.png', dpi=100, bbox_inches='tight')
        plt.clf()


def plot_multiple_automatic_full():
    importpath = './PDF/rawdata/'
    onlyfiles = [placeholder for placeholder in sorted(os.listdir(importpath)) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:    
        importpath = './PDF/' + str(placeholder[:-4]) + '/normal/'
        onlyfiles = [f for f in sorted(os.listdir(importpath)) if isfile(join(importpath, f))]
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[3:]
            f = f[:-20]
            plt.plot(loaded_file[:,0],loaded_file[:,2],'-', label = f)
        plt.xlabel('r / [Å]', fontsize = 15)
        plt.ylabel('G(r)', fontsize = 15)
    plt.yticks([])
    plt.legend(loc='best', ncol=1)
    #plt.xlim(0,37)
    exportpath = './PDF/multiplot/'
    os.mkdir(exportpath[:-1])
    exportpath += '/'
    plt.savefig(exportpath + '01_PDF_rawdata_norm_multi_full.png', dpi=100, bbox_inches='tight')
    plt.clf()
    
def plot_multiple_automatic_cut():
    importpath = './PDF/rawdata/'
    onlyfiles = [placeholder for placeholder in sorted(os.listdir(importpath)) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:    
        importpath = './PDF/' + str(placeholder[:-4]) + '/normal/'
        onlyfiles = [f for f in sorted(os.listdir(importpath)) if isfile(join(importpath, f))]
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[3:]
            f = f[:-20]
            plt.plot(loaded_file[:,0],loaded_file[:,2],'-', label = f)
        plt.xlabel('r / [Å]', fontsize = 15)
        plt.ylabel('G(r)', fontsize = 15)
    plt.yticks([])
    plt.legend(loc='best', ncol=1)
    plt.xlim(0,20)
    exportpath = './PDF/multiplot/'
    plt.savefig(exportpath + '02_PDF_rawdata_norm_multi_cut.png', dpi=100, bbox_inches='tight')    
    plt.clf()
    
    
    