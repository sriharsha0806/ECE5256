#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:31:39 2016

@author: sriharsha0806
"""
# Obtaining Negative Image using the negative transformation
# np.hstack() - used for stacking two different image data of same 
# dimensional into one 
import cv2
import numpy as np
img = cv2.imread('Fig0304(a)(breast_digital_Xray).tif')
cv2.imshow('Original digital mammogram',img)
cv2.waitKey()
maximum = np.amax(img)     # finding the maximum intensity value of image
neg = maximum - img        # Negative trasnformation image
result = np.hstack((img,neg)) # stacking equal dimensional images; we can stack the images in horizontal or vertical
cv2.imshow('negative Vs original',result)
cv2.waitKey()