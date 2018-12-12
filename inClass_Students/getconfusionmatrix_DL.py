#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 15:55:01 2018

@author: mvierlin
"""
import numpy as np


def getconfusionmatrix(Y, T, digit):
    TP = np.sum(np.logical_and(Y[:, digit]==1, T[:, digit]==1))
    TN = np.sum(np.logical_and(Y[:, digit]==0, T[:, digit]==0))
    FP = np.sum(np.logical_and(Y[:, digit]==1, T[:, digit]==0))
    FN = np.sum(np.logical_and(Y[:, digit]==0, T[:, digit]==1))
    
    print('\nConfusion Matrix:\n true positives: %d\n true negatives: %d\n false positives: %d\n false negatives: %d\n'%(TP, TN, FP, FN))
    
    return TP, TN, FP, FN