#!/usr/bin/env python3
# Copyright 2020 Karlsruhe Institute of Technology
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
import os
import subprocess
import pathlib
import tkinter.filedialog as fd

import kadi_apy
from kadi_apy import CLIKadiManager
from tkinter import *

root = Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
#filename = fd.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')

"""The config file is used to get the PAT and host"""
manager = CLIKadiManager()



# global vars
#parentDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run():
    #os.system("pip3 install kadi-apy")
    #result = subprocess.check_output(["pip3","install","kadi-apy"]) 
    #print(result)
    #os.system("pip3 install kadi-apy --upgrade")
    #result = subprocess.check_output(["pip3","install","kadi-apy","--upgrade"]) 
    #print(result)
    #os.system("kadi-apy config create")
    #result = subprocess.check_output(["kadi-apy","config","create"]) 
    #print(result)
    exportpath = './Kadi4mat/User' + '/Adam_Reupert/'
    os.mkdir(exportpath[:-1])
    #os.system("kadi-apy config set-host")
    #result = subprocess.check_output(["kadi-apy","config","set-host"]) 
    #print(result)
    #os.system("https://polis-kadi4mat.iam-cms.kit.edu/")
    #result = subprocess.check_output(["https://polis-kadi4mat.iam-cms.kit.edu/"]) 
    #print(result)
    #os.system("kadi-apy config set-pat")
    #result = subprocess.check_output(["kadi-apy","config","set-pat"]) 
    #print(result)
    #print(os.system("kadi-apy config get-kadi-info"))
    #result = subprocess.check_output(["kadi-apy","config","get-kadi-info"]) 
    #print(result)
    #print(manager.pat_user)    
    
if __name__ == "__main__":
    run()
