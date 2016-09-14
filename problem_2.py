#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:41:01 2016

@author: sriharsha0806
"""
#Four basic images types: dark, light, low,contrast, high contrast and 
# their corresponding histograms
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
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('Fig0316(4)(bottom_left).tif')
# Image 1
cv2.imshow('Dark_image',img)
cv2.waitKey(100)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.figure(1)
plt.title('Histogram of dark image')
plt.show()

# Image 2
img1 = cv2.imread('Fig0316(3)(third_from_top).tif')
cv2.imshow('contrast_image',img1)
cv2.waitKey(100)
hist = cv2.calcHist([img1],[0],None,[256],[0,256])
plt.figure(2)
plt.hist(img1.ravel(),256,[0,256])
plt.title('Histogram of contrast Image')
plt.show()

# Image 3
img2 = cv2.imread('Fig0316(2)(2nd_from_top).tif')
cv2.imshow('low contrast image',img2)
cv2.waitKey(100)
hist = cv2.calcHist([img2],[0],None,[256],[0,256])
plt.figure(3)
plt.hist(img2.ravel(),256,[0,256])
plt.title('Histogram of low contrast image')
plt.show()

# Image 4
img3 = cv2.imread('Fig0316(1)(top_left).tif')
cv2.imshow('light image',img3)
cv2.waitKey(100)
hist = cv2.calcHist([img3],[0],None,[256],[0,256])
plt.figure(4)
plt.hist(img3.ravel(),256,[0,256])
plt.title('histogram of light image')
plt.show()