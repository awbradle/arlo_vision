#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:02:40 2017


https://www.pyimagesearch.com/2014/09/29/finding-brightest-spot-image-using-python-opencv/

https://www.pyimagesearch.com/2016/10/31/detecting-multiple-bright-spots-in-an-image-with-python-and-opencv/


Connected Component Analysis


https://en.wikipedia.org/wiki/Connected-component_labeling


@author: bill
"""

import cv2
import numpy as np
from skimage import measure
from matplotlib import pyplot as plt
import imutils
from imutils import contours
img = cv2.imread('ph.jpg',0)

params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 100
params.maxThreshold = 250


# Filter by Area.
params.filterByArea = True
params.minArea = 10

# Filter by Circularity
#params.filterByCircularity = True
#params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.5
    
# Filter by Inertia
#params.filterByInertia = True
#params.minInertiaRatio = 0.01










detector=cv2.SimpleBlobDetector(params)
cv2.imshow('frame',img)
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
cv2.imshow('blur1',dst)
retval,thresh=cv2.threshold(dst,200,255,cv2.THRESH_BINARY)
cv2.imshow('thresh',thresh)
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=4)
cv2.imshow('thresh after',thresh)



labels = measure.label(thresh, neighbors=4, background=0)
mask = np.zeros(thresh.shape, dtype="uint8")
 
# loop over the unique components
for label in np.unique(labels):
	# if this is the background label, ignore it
	if label == 0:
		continue
 
	# otherwise, construct the label mask and count the
	# number of pixels 
	labelMask = np.zeros(thresh.shape, dtype="uint8")
	labelMask[labels == label] = 255
	numPixels = cv2.countNonZero(labelMask)
 
	# if the number of pixels in the component is sufficiently
	# large, then add it to our mask of "large blobs"
	if numPixels > 100:
		mask = cv2.add(mask, labelMask)
# find the contours in the mask, then sort them from left to
# right
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = contours.sort_contours(cnts)[0]
 
# loop over the contours
for (i, c) in enumerate(cnts):
	# draw the bright spot on the image
	(x, y, w, h) = cv2.boundingRect(c)
	((cX, cY), radius) = cv2.minEnclosingCircle(c)
	cv2.circle(img, (int(cX), int(cY)), int(radius),
		(0, 0, 255), 3)
	cv2.putText(img, "#{}".format(i + 1), (x, y - 15),
		cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
 
# show the output image
cv2.imshow("Image", img)
cv2.waitKey(0)






