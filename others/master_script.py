#!/usr/bin/env python3
# Copyright 2021 Adam Reupert
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Parts of this scripts interact with the POLiS instance of Kadi4mat which is 
# run with the same licence by the Kalrsruher Institute of Technology. 
# Copyright 2020 Karlsruher Institute of Technology (KIT)

"""
Created on Sun Jun 20 17:24:04 2021

@author: Adam Reupert
"""


import os
import pathlib
from kadi_apy import KadiManager


from XRD import xrd_single_routine


#Code start

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
                #raman_routine.baseline_substraction_automatic()
                #raman_routine.normalization_automatic()
                #raman_routine.plot_single_automatic()
                #raman_routine.plot_multiple_automatic_full()
                #raman_routine.plot_multiple_automatic_cut()
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
                xrd_single_routine.simple()               
                break
            elif (module =='2'):
              #  rietfinement_routine.rename_automatic()
              #  rietfinement_routine.normalization_automatic()
              #  rietfinement_routine.plot_single_automatic_full()
              #  rietfinement_routine.plot_single_automatic_cut()
                break
            elif (module =='3'):
              #  pairdisfunc_routine.rename_automatic()
              #  pairdisfunc_routine.normalization_automatic()
              #  pairdisfunc_routine.plot_single_automatic()
              #  pairdisfunc_routine.plot_multiple_automatic_full()
              #  pairdisfunc_routine.plot_multiple_automatic_cut() 
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
             #  nuclearmagres_routine.automatic()
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
                print('happy')
                #   chronoamp_routine.automatic()
            elif (module =='2'):
                print('happy2')
             #   impedance_routine.manual()
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
                print('happy')
                #config.view_settings()
            elif (module =='2'):
                print('happy')
                #config.edit_settings()
            elif (module =='3'):
                print('happy')
                #config.edit_program()
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
                print('happy')
                #questionhelp.raman()
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
