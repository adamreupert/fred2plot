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
from matplotlib.figure import Figure
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
def rename(impdir, expdir):
    importpath = impdir
    onlyfiles = [placeholder for placeholder in listdir(importpath) if isfile(join(importpath, placeholder))]
    for placeholder in onlyfiles:
        loaded_file = np.loadtxt('{}{}'.format(importpath, placeholder))
        exportpath = expdir + str(placeholder)
        if os.path.isdir(exportpath[:-3]) == 0:
            os.mkdir(exportpath[:-3])
        exportpath = expdir + str(placeholder[:-3]) + '/rename/'
        if os.path.isdir(exportpath[:-1]) == 0:
            os.mkdir(exportpath[:-1])
        exportpath += '/'
        np.savetxt('{}{}.csv'.format(exportpath, os.path.splitext(placeholder)[0]), loaded_file, delimiter = ';')   


def baseline_substraction(impdir, expdir):     
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

def normalization(impdir, expdir):
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
def single_plot(impdir, expdir, fig, xlim1, xlim2, ylim1, ylim2):
    importpath = impdir
    onlyfiles = [placeholder for placeholder in listdir(importpath) if isfile(join(importpath, placeholder))]  
    for placeholder in onlyfiles:    
        importpath = expdir + str(placeholder[:-3]) + '/rename/'
        onlyfiles = [f for f in sorted(os.listdir(importpath)) if isfile(join(importpath, f))]
        for f in onlyfiles:
            loaded_file = np.loadtxt('{}{}'.format(importpath, f), delimiter = ';')
            f = f[:-27]
            plot1 = fig.add_subplot(111)
            plot1.plot(loaded_file[:,0],(loaded_file[:,1]),'-',linewidth=0.7, label = f)
            labeltext = f[3:]
            ylim1 = float(ylim1)
            ylim2 = float(ylim2)
            xlim1 = float(xlim1)
            xlim2 = float(xlim2)
            plot1.set_ylim(ylim1,ylim2)
            plot1.set_xlim(xlim1,xlim2)
            plot1.set_xlabel('2 Theta / [°]')
            plot1.set_ylabel('Intensity / [a.u.]')
            plot1.set(yticks=[])
            fig.savefig(expdir + 'singleplot_XRD.svg', dpi=300, bbox_inches='tight')
            return fig
            