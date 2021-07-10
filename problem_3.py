#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:12:34 2016

@author: sriharsha0806
"""
# Histogram Equalization images and their histograms
# np.hstack() - used for stacking two different image data of same 
# dimensional into one 
# cv2.calcHist() calculates the Histogram of an image
# cv2.calcHist() syntax is calcHist(constMat*     images,
#                                   int           nimages,
#                                   const int*    channels,
#                                   inputArray    mask,
#                                   outputArray   hist,
#                                   int           dims,
#                                   const int*    histSize
#                                   const float** ranges
#                                   bool          uniform=true,
#                                   bool          accumulate=false)
#image.ravel()  returns a contiguous flattened array.
# plt.hist() syntax plt.hist(img, bins = #no, range=(#min,#max),fc='k',ec='k')
#cv2.equalizeHist()- A method to improve the contrastness in an image, 
#in order to stretch out the intensity range.
# Equalization means mapping one deistribution to another distribution, so 
# the instensity values are spreaded over the whole range.
#To accomplish the equalization effect, The remapping should be the cumulative 
# distribution function
import cv2
import numpy as np
from matplotlib import pyplot as plt

#image 1
img = cv2.imread('Fig0316(4)(bottom_left).tif',0)
equ = cv2.equalizeHist(img)
cv2.imshow('Dark_image',img)
cv2.waitKey(100)
res = np.hstack((img,equ))
cv2.imwrite('Dark_image.tif',res)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.figure(1)
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram of dark image')
plt.show()
plt.figure(2)
plt.hist(equ.ravel(),256,[0,256])
plt.title('equalized histogram of Dark image')
plt.show()

# image 2
img1 = cv2.imread('Fig0316(3)(third_from_top).tif',0)
equ1 = cv2.equalizeHist(img1)
cv2.imshow('contrast_image',img1)
cv2.waitKey(100)
res1 = np.hstack((img1,equ1))
cv2.imwrite('contrast_image.tif',res1)
hist = cv2.calcHist([img1],[0],None,[256],[0,256])
plt.figure(3)
plt.hist(img1.ravel(),256,[0,256])
plt.title('Histogram of contrast Image')
plt.show()
plt.figure(4)
plt.hist(equ1.ravel(),256,[0,256])
plt.title('equalized Histogram of Contrast Image')

# image 3
img2 = cv2.imread('Fig0316(2)(2nd_from_top).tif',0)
equ2 = cv2.equalizeHist(img2)
res2 = np.hstack((img2,equ2))
cv2.imshow('low contrast image',img2)
cv2.waitKey(100)
res2 = np.hstack((img2,equ2))
cv2.imwrite('low_contrast_image.tif',res2)
hist = cv2.calcHist([img2],[0],None,[256],[0,256])
plt.figure(5)
plt.hist(img2.ravel(),256,[0,256])
plt.title('Histogram of low contrast image')
plt.show()
plt.figure(6)
plt.hist(equ2.ravel(),256,[0,256])
plt.title('equalized histogram of low contrast image')
plt.show()

# image 4
img3 = cv2.imread('Fig0316(1)(top_left).tif',0)
equ3 = cv2.equalizeHist(img3)
res3 = np.hstack((img3,equ3))
cv2.imshow('light image',img3)
cv2.waitKey(100)
cv2.imwrite('light_image.tif',res3)
hist = cv2.calcHist([img3],[0],None,[256],[0,256])
plt.figure(7)
plt.hist(img3.ravel(),256,[0,256])
plt.title('histogram of light image')
plt.show()
plt.figure(8)
plt.hist(equ3.ravel(),256,[0,256])
plt.title('equalized histogram of light image')
plt.show()