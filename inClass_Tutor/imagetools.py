"""
This module provides tools to prepare image data for machine learning tasks.
"""

import matplotlib.pyplot as plt
import numpy as np

def load_pic(filename):
    return plt.imread(filename)

def RGB2Grayscale(img):
    """
    Convert RGB to Grayscale, following https://en.wikipedia.org/wiki/Luma_(video)
    """

    img_gray = 0.2126 * img[:, :, 0] + 0.7152 * img[:, :, 1] + 0.0722 * img[:, :, 2]
    img_gray = img_gray / 255.0 
    return img_gray

def rescale_image(img, m_out, n_out):
    m_in = img.shape[0]
    n_in = img.shape[1]
    
    # get center points
    m_grid_in_aux = np.linspace(0, 1, m_in + 1)
    m_grid_in = (m_grid_in_aux[0:-1] + m_grid_in_aux[1:]) / 2
    
    n_grid_in_aux = np.linspace(0, 1, n_in + 1)
    n_grid_in = (n_grid_in_aux[0:-1] + n_grid_in_aux[1:]) / 2
    
    m_grid_out_aux = np.linspace(0, 1, m_out + 1)
    m_grid_out = (m_grid_out_aux[0:-1] + m_grid_out_aux[1:]) / 2
    
    n_grid_out_aux = np.linspace(0, 1, n_out + 1)
    n_grid_out = (n_grid_out_aux[0:-1] + n_grid_out_aux[1:]) / 2
    
    img_out = np.zeros((m_out, n_out))
    # could be vectorized ...
    for i in range(0, m_out):
        m_idx = np.argmin(np.abs(m_grid_out[i] - m_grid_in)) 
        for j in range(0, n_out):
            n_idx = np.argmin(np.abs(n_grid_out[j] - n_grid_in)) 
            img_out[i, j] = img[m_idx, n_idx] 
            
    return img_out

def convert_MNIST_like(img):
    return np.transpose(np.fliplr(np.transpose(img)))

def thresh_digit(I, sigma=0.5):
    I_out = I.copy()
    I_out[I>sigma] = 1
    I_out[I<=sigma] = 0
    
    return I_out

def load_pic_as_grayscale(filename, show=False, sigma = None):
    img = load_pic(filename)
    img_gray = RGB2Grayscale(img)
    img_resc = rescale_image(img_gray, 28, 28)
    img_MNIST = convert_MNIST_like(img_resc)
    
    if sigma!=None:
        img_MNIST = thresh_digit(img, sigma)
    
    if show:
        plt.imshow(img_MNIST.T)
        plt.colorbar()
        plt.show
    
    return img_MNIST