#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:55:01 2018

@author: mvierlin
"""

import numpy as np
import matplotlib.pyplot as plt

def show_digit(img_vec):
    Neu = img_vec.reshape(28,28)
#    print(Neu)
    plt.imshow(Neu.T)
    
    