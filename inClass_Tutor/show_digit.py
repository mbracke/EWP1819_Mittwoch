import matplotlib.pyplot as plt
import numpy as np

def show_digit(img_vec):
    """
    Display an image with one color channel.
    """
    img = img_vec.reshape(28,28)
    plt.imshow(img.T, interpolation='nearest')
    plt.colorbar()
    plt.show()