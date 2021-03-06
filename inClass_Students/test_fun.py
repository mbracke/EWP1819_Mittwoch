import numpy as np

def f_1D_scipy(x):
    '''
    Funktion 1D
    '''
    f = np.sin(x) ** 3.0
    return f

def dfdx_1D_scipy(x):
    '''
    
    '''
    df = 3.0 * (np.sin(x) **2.0) * np.cos(x)
    return df

def f(x):
    return x**2
