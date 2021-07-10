#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:27:43 2016

@author: sriharsha0806
"""
# Skeleton image and its transformations
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('Fig0343(a)(skeleton_orig).tif',0)
cv2.imshow('img',img)
cv2.waitKey(10000)
laplacian = cv2.Laplacian(img,cv2.CV_64F) 
sharp = img + laplacian
sobel_x = cv2.Sobel(img,cv2.CV_64F,1,0)
sobel_y = cv2.Sobel(img,cv2.CV_64F,0,1)
sobel = np.hypot(sobel_x,sobel_y)
avg_sobel = cv2.blur(sobel,(5,5))
sobel_mask = np.multiply(sharp,avg_sobel)
sum_sobel = sobel_mask+img
power_law = np.power(sum_sobel,0.5);
plt.figure(1)
plt.subplot(2,2,1),plt.imshow(img, cmap = plt.cm.binary),plt.title('original Image')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian, cmap = plt.cm.binary),plt.title('Laplacian')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sharp, cmap = plt.cm.binary),plt.title('sharpened image')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobel, cmap = plt.cm.binary),plt.title('sobel gradient of Original Image')
plt.xticks([]),plt.yticks([])
plt.figure(2)
plt.subplot(2,2,1),plt.imshow(avg_sobel, cmap = plt.cm.binary),plt.title('sobel image avg mask')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(sobel_mask, cmap = plt.cm.binary),plt.title('Masking sobel with sharp')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sum_sobel, cmap = plt.cm.binary),plt.title('sum of original+sum_sobel')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(power_law, cmap = plt.cm.binary),plt.title('power law transformation')
plt.xticks([]),plt.yticks([])
plt.show()