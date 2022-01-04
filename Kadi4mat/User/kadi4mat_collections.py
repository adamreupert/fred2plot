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
    Kadi_module()
    """Create collection resources."""
    CARC_collection()
    VS4_collection()
    FeS2_collection()
    TiS3_collection()
    
    """Create record resources."""
    # identi = "VS4_0000002_001_001_XRD"
    # tit = "VS4_0000002_001_001_XRD"
    # sample_records()
    

def Kadi_module():
    #os.system("pip3 install kadi-apy")
    result = subprocess.check_output(["pip3","install","kadi-apy"]) 
    print(result)
    #os.system("pip3 install kadi-apy --upgrade")
    result = subprocess.check_output(["pip3","install","kadi-apy","--upgrade"]) 
    print(result)
    #os.system("kadi-apy config create")
    result = subprocess.check_output(["kadi-apy","config","create"]) 
    print(result)
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

    
def CARC_collection():
    
    # Creation / checking of CARC material collection
    identifier = "CARC_materials"
    title = "CARC materials"
    collection = manager.collection(identifier=identifier, title=title, create=True)
    # Editing of collection
    description = "Collection for all materials that feature the joint cationic anionic redox chemistry (CARC). CARC principle: By overlapping the 3d band (transition metal) and the 3p band (sulfur) it enables more electrons that can participate in the process of insertion of a magnesium ion into the host structure. This leads to a lower diffusion barrier enabling higher movement within the host structure."
    collection.edit(description = description)
    collection.add_tag(tag = "redox chemistry")
    collection.add_tag(tag = "multivalent")
    collection.add_tag(tag = "magnesium")
    collection.add_tag(tag = "calcium")
    collection.add_tag(tag = "cathode")
    collection.add_tag(tag = "VS4")
    collection.add_tag(tag = "TiS3")
    collection.add_tag(tag = "FeS2")
    CARC_collection_id = collection.id
    print("Sample collection created/updated successfully.")
    
def VS4_collection():
    identifier = "VS4_materials"
    title = "VS4 materials"
    collection = manager.collection(identifier=identifier, title=title, create=True)
    # Editing of collection
    description = "Collection of all materials, measurements and processes that were used and/or obtained with the goal to synthesize and characterize VS4. VS4 enables a high amount of Mg-ion insertion (>1 per formula) and by using the CARC principle also should facilitate higher charging rates than comparable conventional cathode materials."
    collection.edit(description = description)
    collection.add_tag(tag = "redox chemistry")
    collection.add_tag(tag = "multivalent")
    collection.add_tag(tag = "magnesium")
    collection.add_tag(tag = "calcium")
    collection.add_tag(tag = "cathode")
    collection.add_tag(tag = "VS4")
    collection.add_tag(tag = "Vanadium sulfides")
    collection.add_tag(tag = "Vanadium")
    collection.add_tag(tag = "Sulfur")
    collection.add_tag(tag = "Patronite")
    collection.add_tag(tag = "CARC")
    VS4_collection_id = collection.id
    print("VS4 collection created/updated successfully.")

def FeS2_collection():
    identifier = "FeS2_materials"
    title = "FeS2 materials"
    collection = manager.collection(identifier=identifier, title=title, create=True)
    # Editing of collection
    description = "Collection of all materials, measurements and processes that were used and/or obtained with the goal to synthesize and characterize FeS2. By using the CARC principle, FeS2 should facilitate higher charging rates than comparable conventional cathode materials. By using iron and sulfur as educts, this material would be very cheap and environmentally firendly."
    collection.edit(description = description)
    collection.add_tag(tag = "redox chemistry")
    collection.add_tag(tag = "multivalent")
    collection.add_tag(tag = "magnesium")
    collection.add_tag(tag = "calcium")
    collection.add_tag(tag = "cathode")
    collection.add_tag(tag = "FeS2")
    collection.add_tag(tag = "Iron sulfides")
    collection.add_tag(tag = "Iron")
    collection.add_tag(tag = "Sulfur")
    collection.add_tag(tag = "Pyrite")
    collection.add_tag(tag = "CARC")
    FeS2_collection_id = collection.id
    print("FeS2 collection created/updated successfully.")

def TiS3_collection():
    identifier = "TiS3_materials"
    title = "TiS3 materials"
    collection = manager.collection(identifier=identifier, title=title, create=True)
    # Editing of collection
    description = "Collection of all materials, measurements and processes that were used and/or obtained with the goal to synthesize and characterize TiS3. By using the CARC principle, TiS3 should facilitate higher charging rates than comparable conventional cathode materials. By using titanium and sulfur as educts, this material would be very cheap and environmentally firendly."
    collection.edit(description = description)
    collection.add_tag(tag = "redox chemistry")
    collection.add_tag(tag = "multivalent")
    collection.add_tag(tag = "magnesium")
    collection.add_tag(tag = "calcium")
    collection.add_tag(tag = "cathode")
    collection.add_tag(tag = "TiS3")
    collection.add_tag(tag = "Titanium sulfides")
    collection.add_tag(tag = "Titanium")
    collection.add_tag(tag = "Sulfur")
    collection.add_tag(tag = "CARC")
    TiS3_collection_id = collection.id
    print("TiS3 collection created/updated successfully.")
    
def sample_records():
    
    # Record.
    identifier = identi
    title = tit
    record = manager.record(identifier=identifier, title=title, create=True)
    
    # Editing of record
    description = "XRD measurement of pristine VS4 at a Stoe Stadi p Instrument"
    record.edit(type = "XRD_data", description = description)
    
    # Tagging
    record.add_tag(tag = "XRD measurement")
    record.add_tag(tag = "capillary")
    record.add_tag(tag = "Debye-Scherrer")
    record.add_tag(tag = "Molybdenum")
    record.add_tag(tag = "pristine")
    record.add_tag(tag = "VS4")
    
    # Addition of files to the record
    filelocation = fd.askopenfilename(parent=root, initialdir=currdir, title='Please select Rawdata')
    if len(filelocation) > 0:
        record.upload_file(filelocation, file_name = "Rawdata")
    filelocation = fd.askopenfilename(parent=root, initialdir=currdir, title='Please select a XY')
    if len(filelocation) > 0:
        record.upload_file(filelocation, file_name = "XY")
    filelocation = fd.askopenfilename(parent=root, initialdir=currdir, title='Please select a uncut Plot')
    if len(filelocation) > 0:
        record.upload_file(filelocation, file_name = "plot_uncut")
    filelocation = fd.askopenfilename(parent=root, initialdir=currdir, title='Please select a cut Plot')
    if len(filelocation) > 0:
        record.upload_file(filelocation, file_name = "plot_cut")
    
    # Metadata of first record.
    metadata = [
        {"key": "sample",  "type": "str",   "value": "VS4"},
        {"key": "radiation source", "type": "str", "value": "Molybdenum"},
        {"key": "characteristic radiation used", "type": "str", "value": "K-apha1"},
        {"key": "X-Ray tube voltage",   "type": "int", "value":  50, "unit": "V"},
        {"key": "X-Ray tube current",   "type": "int", "value":  40, "unit": "mA"},
        {"key": "measurement mode", "type": "str",   "value": "Debye-Scherrer"},
        {"key": "2Theta-Omega", "type": "str", "value": "fixed"},
        {"key": "capillary supplier", "type": "str",   "value": "Hilgenberg"},
        {"key": "capillary material", "type": "str",   "value": "Soda lime glass"},
        {"key": "capillary diameter",   "type": "float", "value":  0.7, "unit": "mm"},
        {"key": "capillary wall thickness",   "type": "float", "value":  0.01, "unit": "mm"},
        {"key": "measurement range beginn",   "type": "float", "value":  4.5, "unit": "°"},
        {"key": "measurement range end",   "type": "float", "value":  61.0, "unit": "°"},
        {"key": "step size",   "type": "float", "value":  1, "unit": "°"},
        {"key": "step time",   "type": "int", "value":  60, "unit": "s"},
        ]
    record.add_metadata(metadata, force=True)
    record.add_collection_link(manager.collection(identifier = "CARC_materials", title = "CARC materials").id)
    
    
    identifier = "stoe-stadi-p-xrd-instrument-int-bldg717-r107"
    title = "Stoe Stadi P XRD Instrument (INT-Bldg.717-R107)"
    record = manager.record(identifier=identifier, title=title, create=True)
    record.link_record(manager.record(identifier = identi, title = tit).id, name = "measurement")
    
    # # Addition of Members
    # username = "eschoof"
    # identity_type = "ldap"
    # schoof = manager.user(username= username, identity_type = identity_type).id
    # manager.collection(identifier = "CARC_materials", title = "CARC materials").add_user(user_id = schoof, role_name = "member")
    # manager.record(identifier = "VS4_001_001_001_mat", title = "Vanadium(IV)-sulfide").add_user(user_id = schoof, role_name = "member")
    # manager.record(identifier = "VS4_001_001_001_XRD", title = "Vanadium(IV)-sulfide_XRD").add_user(user_id = schoof, role_name = "member")
    # manager.record(identifier = "RDM-Workshop_script", title = "Workflow script").add_user(user_id = schoof, role_name = "member")
    # print("Ephraim added successfully.")


if __name__ == "__main__":
    run()



#file location
#absFilePath = os.path.abspath(__file__)
#print(absFilePath)

