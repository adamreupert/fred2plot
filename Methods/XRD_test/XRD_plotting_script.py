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

#Different processing blocks XRD
def rename_automatic_XRD():
    importpath = './0_xy/'
    onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
    for f in onlyfiles:
        loaded_file = np.loadtxt('{}{}'.format(importpath, f))
        exportpath = './' + str(f)
        os.mkdir(exportpath[:-3])
        exportpath = './' + str(f[:-3]) + '/rename/'
        os.mkdir(exportpath[:-1])
        exportpath += '/'
        np.savetxt('{}{}.csv'.format(exportpath, os.path.splitext(f)[0]), loaded_file, delimiter = ';')      
def baseline_substraction_automatic_XRD():     
    importpath = './0_xy/'
    onlyfiles = [placeholder for placeholder in listdir(importpath) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:    
        importpath = './' + str(placeholder[:-3]) + '/rename/'
        onlyfiles = [f for f in listdir(importpath) if isfile(join(importpath, f))]
        for f in onlyfiles:
            my_data = []    
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            my_data.append(loaded_file[:,0])
            my_data.append(loaded_file[:,1])
            my_data.append(baseline_als(loaded_file[:,1], 1000000, 0.001))
            my_data.append(loaded_file[:,1] - baseline_als(loaded_file[:,1], 1000000, 0.001))
            result = np.array(my_data)
            result = result.T   
            exportpath = './' + str(placeholder[:-3]) + '/baseline/'
            os.mkdir(exportpath[:-1])
            exportpath += '/'
            np.savetxt('{}{}_basecorr.csv'.format(exportpath, os.path.splitext(f)[0]), result, delimiter = ';')    
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
            dataline = ax1.plot(loaded_file[:,0],(loaded_file[:,5]+addition),'-',linewidth=0.7, label = f)
            dataline
            labeltext = f[3:]
            ax1.set_xlim(4.5,35)
            ax1.text((ax1.get_xlim()[1]-(ax1.get_xlim()[1]*0.025)), 0.5 + addition, labeltext, color= dataline[0].get_color(),ha = 'right')
            addition = addition - 1.1
            ax1.set_xlabel('2 Theta / [°]')
            ax1.set_ylabel('Intensity / [a.u.]')
            ax1.set(yticks=[])
            #ax1.text(-0.08, 0.97, string.ascii_uppercase[0]+')', transform=ax1.transAxes, size=15)
    fig.subplots_adjust(hspace=0.25)
    exportpath = './'  
    plt.savefig(exportpath + 'VS4_001_001_001_XRD.svg', dpi=300, bbox_inches='tight')
    plt.savefig(exportpath + 'VS4_001_001_001_XRD.png', dpi=300, bbox_inches='tight')
#program
rename_automatic_XRD()
baseline_substraction_automatic_XRD()
normalization_automatic_XRD()
plot()

