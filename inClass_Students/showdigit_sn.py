#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:05:21 2018

@author: nstelzne
"""

import numpy as np
import matplotlib.pyplot as plt

def show_digit(img_vec):
    m=np.zeros((28,28))
    for i in range(0,28):
        m[:,i]=img_vec[28*i:28*i+28]
    plt.imshow(m)
    return m