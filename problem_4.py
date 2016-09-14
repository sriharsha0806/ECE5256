#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:25:09 2016

@author: sriharsha0806
"""
# Noise Reduction using averaging Mask and Median filter
# cv2.blur() is used for smoothing images
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('Fig0335(a)(ckt_board_saltpep_prob_pt05).tif')
avg_Mask = cv2.blur(img,(3,3))
median = cv2.medianBlur(img,3)
plt.figure(1)
plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(avg_Mask),plt.title('3X3 averaging mask')
plt.xticks([]),plt.yticks([])
plt.subplot(133),plt.imshow(median),plt.title('3X3 median filter')
plt.xticks([]),plt.yticks([])
plt.show()