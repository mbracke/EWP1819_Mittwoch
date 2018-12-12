#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:51:46 2018

@author: nstelzne
"""

def getconfusionmatrix(Y, T, digit):
    TP = np.sum(np.logical_and(Y[:, digit]==1, T[:, digit]==1))
    # your turn
    TN = np.sum(np.logical_and(np.logical_not(Y[:, digit]==1), T[:, digit]==1))
    
    FP = np.sum(np.logical_and(Y[:, digit]==1, np.logical_not(T[:, digit]==1)))
    FN = np.sum(np.logical_and(np.logical_not(Y[:, digit]==1), np.logical_not(T[:, digit]==1)))
    
                
    print('\nConfusion Matrix:\n true positives: %d\n true negatives: %d\n false positives: %d\n false negatives: %d\n'%(TP, TN, FP, FN))
    
    return TP, TN, FP, FN