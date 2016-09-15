# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 01:22:08 2016

@author: sriharsha0806
"""

# import required packages
import matplotlib.pyplot as plt
import numpy as np
import skimage.io as io
from skimage.exposure import equalize_hist
from skimage.color import rgb2gray
#%matplotlib inline

# Read Images
# Mandrill image
mandrill = io.imread('mandrill.png')
image = mandrill
io.imshow(mandrill)
io.show()


#Lenna image
lena = io.imread('lena.png')
io.imshow(lena)
io.show()

# Defining a function to display multiple images
def show_images(images,titles=None):
    """Display a List of images"""
    n_ims = len(images)
    if titles is None: titles = ['(%d)' %i for i in range(1,n_ims+1)]
    fig = plt.figure()
    n=1
    for image,title in zip(images,titles):
        a = fig.add_subplot(1,n_ims,n) # Make subplot
        if image.ndim == 2:                           # Is image grayscale?
            plt.gray() 
        plt.imshow(image)
        a.set_title(title)
        n += 1
    fig.set_size_inches(np.array(fig.get_size_inches())*n_ims)
    plt.show()

# create an image (10X10 pixels)
rgb_image = np.zeros(shape=(10,10,3), dtype=np.uint8) #unsigned 8 bit int
rgb_image[:,:,0]=255 # set red value for all pixels
rgb_image[:,:,1]=255 # set green value for all pixels
rgb_image[:,:,2]=0 # set blue value for all pixels
show_images(images=[rgb_image],titles=["Red plus Green equals..."])

# show_images
red,green,blue=image.copy(),image.copy(),image.copy()
red[:,:,(1,2)] = 0
green[:,:,(0,2)]=0
blue[:,:,(0,1)]=0
show_images(images=[red, green, blue],titles=['Red Intensity', 'Green Intensity', 'Blue Intensity'])
print('Note:lighter areas correspond to higher intensities\n')

# Grayscaling

gray_image = rgb2gray(image)
show_images(images=[image,gray_image],
            titles = ["Color","GrayScale"])

# Histogram equalization

equalized_image = equalize_hist(gray_image)
show_images(images=[gray_image, equalized_image],
            titles=["Grayscale","Histogram Equalized"])
            