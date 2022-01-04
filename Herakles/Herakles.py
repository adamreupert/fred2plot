#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:50:50 2020

@author: Adam Reupert
"""

#Code start


#Import section
from Setupfiles import raman_routine

from Setupfiles import PXRD_routine
from Setupfiles import rietfinement_routine
from Setupfiles import pairdisfunc_routine

from Setupfiles import nuclearmagres_routine

from Setupfiles import chronoamp_routine
from Setupfiles import impedance_routine

from Setupfiles import config
from Setupfiles import questionhelp


#Module selection
print('Welcome to the raw data treatment program')
while True:
    print('Which program would you like to load?')
    print('[1] Raman')
    print('[2] Diffraction')
    print('[3] Nuclear magnetic resonance')
    print('[4] Electrochemical measurements')
    print('[8] Edit Configfile')
    print('[9] Help')
    print('[q] Quit')
    module = str(input('(1/2/3/4/8/9/q):'))
      
    
    
    if (module =='1'):
        print('Welcome to the Raman program')
        while True:
            print('How would you like to proceed?')
            print('[1] Automatic')
            print('[q] Return')
            module = str(input('(1/q):'))
            if (module =='1'):
                raman_routine.rename_automatic()
                raman_routine.baseline_substraction_automatic()
                raman_routine.normalization_automatic()
                raman_routine.plot_single_automatic()
                raman_routine.plot_multiple_automatic_full()
                raman_routine.plot_multiple_automatic_cut()
                break
            elif (module.lower() == 'q' or module.lower() == 'quit'):
                module = ('')
                print('Closing application')
                break
            else:
                print('No valid entry, please use one of the prompted options!')
    
    
    
    elif (module =='2'):
        print('Welcome to the diffraction program')
        while True:
            print('What kind of diffraction data do you want to process?')
            print('[1] PXRD')
            print('[2] Rietveld')
            print('[3] Pair distribution function')
            print('[q] Return')
            module = str(input('(1/2/3/q):'))
            if (module =='1'):
                PXRD_routine.rename_automatic()
                PXRD_routine.baseline_substraction_automatic()
                PXRD_routine.normalization_automatic()
                PXRD_routine.plot_single_automatic()
                PXRD_routine.plot_multiple_automatic_full()
                PXRD_routine.plot_multiple_automatic_cut()                
                break
            elif (module =='2'):
                rietfinement_routine.rename_automatic()
                rietfinement_routine.normalization_automatic()
                rietfinement_routine.plot_single_automatic_full()
                rietfinement_routine.plot_single_automatic_cut()
                break
            elif (module =='3'):
                pairdisfunc_routine.rename_automatic()
                pairdisfunc_routine.normalization_automatic()
                pairdisfunc_routine.plot_single_automatic()
                pairdisfunc_routine.plot_multiple_automatic_full()
                pairdisfunc_routine.plot_multiple_automatic_cut() 
                break
            elif (module.lower() == 'q' or module.lower() == 'quit'):
                module = ('')
                print('Closing application')
                break
            else:
                print('No valid entry, please use one of the prompted options!')
    
    
    
    elif (module =='3'):
        print('Welcome in the nuclear magnetic resonance program')
        while True:
            print('How would you like to proceed?')
            print('[1] Automatic')
            print('[q] Return')
            module = str(input('(1/q):'))
            if (module =='1'):
                nuclearmagres_routine.automatic()
                break
            elif (module.lower() == 'q' or module.lower() == 'quit'):
                module = ('')
                print('Closing application')
                break
            else:
                print('No valid entry, please use one of the prompted options!')
    
    
    
    elif (module =='4'):
        print('Welcome to the electrochemical measurement program')
        while True:
            print('What kind of data do you want to process?')
            print('[1] Chronoamperometry')
            print('[2] Potentiostatic electrocemical impedance spectroscopy')
            print('[q] Return')
            module = str(input('(1/2/q):'))
            if (module =='1'):
                chronoamp_routine.automatic()
            elif (module =='2'):
                impedance_routine.manual()
            elif (module.lower() == 'q' or module.lower() == 'quit'):
                module = ('')
                print('Closing application')
                break
            else:
                print('No valid entry, please use one of the prompted options!')
    
    
    elif (module =='8'):
        print('Welcome to the config modifier')
        while True:
            print('How would you like to proceed?')
            print('[1] View parameters')
            print('[2] Edit parameters')
            print('[3] Edit programs')
            print('[q] Return')
            module = str(input('(1/2/q):'))
            if (module =='1'):
                config.view_settings()
            elif (module =='2'):
                config.edit_settings()
            elif (module =='3'):
                config.edit_program()
            elif (module.lower() == 'q' or module.lower() == 'quit'):
                module = ('')
                print('Closing application')
                break
            else:
                print('No valid entry, please use one of the prompted options!')        
    
    
    
    elif (module =='9' or module.lower() == 'h' or module.lower() == 'help'):
        print('Welcome in the help section')
        while True:
            print('What are you looking for?')
            print('[1] Raman')
            print('[2] ...')
            print('[q] Return')
            module = str(input('(1/2/q):'))
            if (module =='1'):
                questionhelp.raman()
                pass
            elif (module =='2'):
                pass
            elif (module.lower() == 'q' or module.lower() == 'quit'):
                module = ('')
                print('Closing application')
                break
            else:
                print('No valid entry, please use one of the prompted options!')        
    
    
    
    elif (module.lower() == 'q' or module.lower() == 'quit'):
        module = ('')
        print('Bye Bye')
        break
    
    
    
    else:
        print('No valid entry, please use one of the prompted options!')
             
#Code end
        