#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:51:10 2019

@author: isa
"""

import os #optional
from matplotlib.image import imread
import numpy as np

#filepath = '/home/isa/Escritorio/test'
#
#if os.path.exists(filepath): #optional check if file exists
#    a=[];
#    for files in filepath:
#           img= imread(files)
#           a.append(img)
#           np.asarray(a)
#
#
#           print(files)
        
a=[];
filepath = '/home/isa/Escritorio/train'
for filename in os.listdir(filepath):    
   img= imread(filepath+'/'+filename)
   a.append(img)
a = np.asarray(a)
print(a)