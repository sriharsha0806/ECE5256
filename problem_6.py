# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:06:43 2016

@author: sriharsha0806
"""

import skimage.io as io
import numpy as np
#%matplotlib inline
from matplotlib import pyplot as plt
from skimage.filters import gaussian
from skimage.filters import laplace
from skimage.filters import sobel_h
from skimage.filters import sobel_v
img = io.imread('Fig0343(a)(skeleton_orig).tif',0) # Original Image
# Lapalcian
laplacian = laplace(img)

#sharp image is obtained by adding original and laplacian image
sharp = np.add(img,laplacian)

# sobel gradient of original Image
img1 = sobel_h(img)
img2 = sobel_v(img)
imres = np.hypot(img1,img2)
# sobel image smoothed with a 5X5 averaging 
Average = gaussian(img,5)

# Mask image by multiplying sharpened image with average
Mask  = np.multiply(Average,sharp) 

# Sharpened image obtained by sum of original image and Mask image
sharp_1 = np.add(img,Mask)

#power transformation
power = np.sqrt(sharp_1)

plt.figure(1)
plt.subplot(2,2,1),plt.imshow(img, cmap = plt.cm.bone),plt.title('Original_Image')
plt.xticks([]),plt.xticks([])
plt.subplot(2,2,2),plt.imshow(laplacian, cmap = plt.cm.bone),plt.title('Lapalacian of Image')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sharp, cmap = plt.cm.bone),plt.title('sharpened Image')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(imres, cmap = plt.cm.bone),plt.title('sobel gradient of image')
plt.xticks([]),plt.yticks([])
plt.show()

plt.figure(2)
plt.subplot(2,2,1),plt.imshow(Average, cmap = plt.cm.bone), plt.title('Average5_sobel')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(Mask, cmap = plt.cm.bone),plt.title('Masked Image')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sharp_1, cmap = plt.cm.bone),plt.title('sharepened')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(power, cmap = plt.cm.bone),plt.title('Power Transformation')
plt.xticks([]),plt.yticks([])
plt.show()

"""
plt.figure(3)
plt.subplot(2,2,1),plt.imshow(255 - img, cmap = plt.cm.binary),plt.title('Original_Image')
plt.xticks([]),plt.xticks([])
plt.subplot(2,2,2),plt.imshow(255 - laplacian, cmap = plt.cm.binary),plt.title('Lapalacian of Image')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(255 - sharp, cmap = plt.cm.binary),plt.title('sharpened Image')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(255 - imres, cmap = plt.cm.binary),plt.title('sobel gradient of image')
plt.xticks([]),plt.yticks([])
plt.show()

plt.figure(3)
plt.subplot(2,2,1),plt.imshow(255 - Average, cmap = plt.cm.binary), plt.title('Average5_sobel')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(255 - Mask, cmap = plt.cm.binary),plt.title('Masked Image')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(255 - sharp_1, cmap = plt.cm.binary),plt.title('sharepened')
plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(255 - power, cmap = plt.cm.binary),plt.title('Power Transformation')
plt.xticks([]),plt.yticks([])
plt.show()
"""
