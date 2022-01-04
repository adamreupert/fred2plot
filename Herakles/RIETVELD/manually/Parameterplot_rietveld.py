#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:44:33 2020

@author: adam
"""

import matplotlib.pyplot as plt
import numpy as np


radii = [167,170,182]
cellparama = [6.952966,6.95282,6.966143]
cellparamc = [7.093006,7.09732,7.120039]
cellvol = [342.902410909,340.40462,345.51518834]

#plt.plot(radii,cellparama, '-', label ='a')
plt.plot(radii,cellvol, label ='Cell volume')
#plt.plot(167,6.952966, 'sr', label ='Cl-')
plt.plot(167,342.902410909, 's', label ='Cl-')
#plt.plot(170,6.95282, 'sg', label ='S2-')
plt.plot(170,340.40462, 's', label ='S2-')
#plt.plot(182,6.966143, 'sb', label ='Br-')
plt.plot(182,345.51518834, 's', label ='Br-')

plt.xlabel('Anion radii / [pm]',fontsize = 15)
plt.ylabel('Cell volume / [Å³]',fontsize = 15)

plt.legend(loc='best')
#handles,labels = ax.get_legend_handles_labels()
#ax.legend(labels, loc='upper center', bbox_to_anchor=(1.5, 1.5),ncol=3, fancybox=True, shadow=True)
#plt.show()
plt.savefig('cellparamc_plot.png', dpi=100)