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
from Setupfiles import config
import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from scipy.sparse.linalg import spsolve



#Code section ---------------------------------------------

#Internal functions
#Algorithm called "Asymmetric Least Squares Smoothing" by P. Eilers and H. Boelens, published in 2005.
def baseline_als(y, lam, asymmetry, n_iter=10):
  L = len(y)
  D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
  w = np.ones(L)
  for i in range(n_iter):
    W = sparse.spdiags(w, 0, L, L)
    Z = W + lam * D.dot(D.transpose())
    z = spsolve(Z, w*y)
    w = asymmetry * (y > z) + (1-asymmetry) * (y < z)
  return z

#Different processing blocks
def rename_automatic():
    importpath = './RAMAN/rawdata/'
    onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
    for f in onlyfiles:
        loaded_file = np.loadtxt('{}{}'.format(importpath, f),delimiter = '	')
        exportpath = './RAMAN/' + str(f)
        os.mkdir(exportpath[:-4])
        exportpath = './RAMAN/' + str(f[:-4]) + '/rename/'
        os.mkdir(exportpath[:-1])
        exportpath += '/'
        np.savetxt('{}{}.csv'.format(exportpath, os.path.splitext(f)[0]), loaded_file, delimiter = ';')

        
def baseline_substraction_automatic():     
    importpath = './RAMAN/rawdata/'
    onlyfiles = [placeholder for placeholder in listdir(importpath) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:    
        importpath = './RAMAN/' + str(placeholder[:-4]) + '/rename/'
        onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
        for f in onlyfiles:
            my_data = []    
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            my_data.append(loaded_file[:,0])
            my_data.append(loaded_file[:,1])
            my_data.append(baseline_als(loaded_file[:,1], config.baseline_lambda, config.baseline_asymmetry))
            my_data.append(loaded_file[:,1] - baseline_als(loaded_file[:,1], config.baseline_lambda, config.baseline_asymmetry))
            result = np.array(my_data)
            result = result.T   
            exportpath = './RAMAN/' + str(placeholder[:-4]) + '/baseline/'
            os.mkdir(exportpath[:-1])
            exportpath += '/'
            np.savetxt('{}{}_basecorr.csv'.format(exportpath, os.path.splitext(f)[0]), result, delimiter = ';')    
    
        

def normalization_automatic():
    importpath = './RAMAN/rawdata/'
    onlyfiles = [placeholder for placeholder in listdir(importpath) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:    
        importpath = './RAMAN/' + str(placeholder[:-4]) + '/baseline/'
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
            exportpath = './RAMAN/' + str(placeholder[:-4]) + '/normal/'
            os.mkdir(exportpath[:-1])
            exportpath += '/'
            np.savetxt('{}{}_normal.csv'.format(exportpath, os.path.splitext(f)[0]), result, delimiter = ';')
 
    
def plot_single_automatic():
    importpath = './RAMAN/rawdata/'
    onlyfiles = [placeholder for placeholder in listdir(importpath) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:    
        importpath = './RAMAN/' + str(placeholder[:-4]) + '/normal/'
        
        
        onlyfiles = [f for f in sorted(os.listdir(importpath)) if isfile(join(importpath, f))]
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[3:]
            f = f[:-20]
            plt.plot(loaded_file[:,0],loaded_file[:,1],'-', label = f)
        plt.xlabel('Wave number / [cm-1]', fontsize = 15)
        plt.ylabel('Intensity / [a.u.]', fontsize = 15)
        plt.yticks([])
        plt.legend(bbox_to_anchor=(-0.01, 1.35), loc='upper left', ncol=2)
        plt.gca().invert_xaxis()
        #plt.xlim(800,100)
        exportpath = './RAMAN/' + str(placeholder[:-4]) + '/plot/'
        os.mkdir(exportpath[:-1])
        exportpath += '/'
        plt.savefig(exportpath + '01_raman_rawdata.png', dpi=100, bbox_inches='tight')
        plt.clf()
        
        
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[3:]
            f = f[:-20]
            plt.plot(loaded_file[:,0],(loaded_file[:,1]),'-', label = f)
            plt.plot(loaded_file[:,0],(loaded_file[:,2]),'-', label = f)
        plt.xlabel('Wave number / [cm-1]', fontsize = 15)
        plt.ylabel('Intensity / [a.u.]', fontsize = 15)
        plt.yticks([])
        plt.legend(bbox_to_anchor=(-0.01, 1.35), loc='upper left', ncol=2)
        plt.gca().invert_xaxis()
        #plt.xlim(800,100)
        plt.savefig(exportpath + '02_raman_baselinecorrection.png', dpi=100, bbox_inches='tight')
        plt.clf()
        
        
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[3:]
            f = f[:-20]
            plt.plot(loaded_file[:,0],loaded_file[:,5],'-', label = f)
        plt.xlabel('Wave number / [cm-1]', fontsize = 15)
        plt.ylabel('Intensity / [a.u.]', fontsize = 15)
        plt.yticks([])
        plt.legend(bbox_to_anchor=(-0.01, 1.35), loc='upper left', ncol=2)
        plt.gca().invert_xaxis()
        #plt.xlim(800,100)
        plt.savefig(exportpath + '03_raman_corr_norm.png', dpi=100, bbox_inches='tight')
        plt.clf()

def plot_multiple_automatic_full():
    importpath = './RAMAN/rawdata/'
    onlyfiles = [placeholder for placeholder in sorted(os.listdir(importpath)) if isfile(join(importpath, placeholder))]
    addition = 0
    for placeholder in onlyfiles:    
        importpath = './RAMAN/' + str(placeholder[:-4]) + '/normal/'
        onlyfiles = [f for f in sorted(os.listdir(importpath)) if isfile(join(importpath, f))]
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[3:]
            f = f[:-20]
            plt.plot(loaded_file[:,0],(loaded_file[:,5]+addition),'-', label = f)
            addition = addition + 1.2
    plt.gca().invert_xaxis()
    plt.xlabel('Wave number / [cm-1]', fontsize = 15)
    plt.ylabel('Intensity / [a.u.]', fontsize = 15)
    plt.yticks([])
    plt.legend(bbox_to_anchor=(-0.01, 1.35), loc='upper left', ncol=2)
    exportpath = './RAMAN/multiplot/'
    os.mkdir(exportpath[:-1])
    exportpath += '/'
    plt.savefig(exportpath + '01_raman_rawdata_corr_norm_multi_full.png', dpi=100, bbox_inches='tight')
    plt.clf()
    
def plot_multiple_automatic_cut():
    importpath = './RAMAN/rawdata/'
    onlyfiles = [placeholder for placeholder in sorted(os.listdir(importpath)) if isfile(join(importpath, placeholder))]
    addition = 0
    for placeholder in onlyfiles:    
        importpath = './RAMAN/' + str(placeholder[:-4]) + '/normal/'
        onlyfiles = [f for f in sorted(os.listdir(importpath)) if isfile(join(importpath, f))]
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[3:]
            f = f[:-20]
            plt.plot(loaded_file[:,0],(loaded_file[:,5]+addition),'-', label = f)
            addition = addition + 1.2
    plt.xlim(750,100)
    plt.xlabel('Wave number / [cm-1]', fontsize = 15)
    plt.ylabel('Intensity / [a.u.]', fontsize = 15)
    plt.yticks([])
    plt.legend(bbox_to_anchor=(-0.01, 1.35), loc='upper left', ncol=2)
    exportpath = './RAMAN/multiplot/'
    plt.savefig(exportpath + '02_raman_rawdata_corr_norm_multi_cut.png', dpi=100, bbox_inches='tight')

