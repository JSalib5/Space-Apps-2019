from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random as rng
import matplotlib.pyplot as plt
from astropy.io import fits


rng.seed(12345)
def thresh_callback(val, image):
    threshold = val
    canny_output = cv.Canny(image, threshold, threshold * 2)
    z = canny_output
    contours, hierachy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours_poly = [None] * len(contours)
    boundRect = [None] * len(contours)
    centers = [None] * len(contours)
    radius = [None] * len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i])
    return z, centers

"""
src = np.uint8(fits.getdata(r'Images/NEOS_SCI_2019002002143_clean.fits', ext=0))
src2 = np.uint8(fits.getdata(r'Images/NEOS_SCI_2019002002349_clean.fits', ext=0))

print(src)
"""
#cv.imwrite("name3.png", data)
src = cv.imread("2019day129-11.png")
src2 = cv.imread("2019day129-12.png")

img1 = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
img1 = cv.blur(src, (3, 3))

img2 = cv.cvtColor(src2, cv.COLOR_BGR2GRAY)
img2 = cv.blur(src2, (3, 3))

#participant or viewer

thresh = 100  # initial threshold

z1, c1 = thresh_callback(thresh, img1)
z2, c2 = thresh_callback(thresh, img2)

#cv.imwrite("names.png", z1)
#cv.imwrite("name-1.png", z2)

changed_objects_initial = []
changed_objects_final = []

c1 = list(set(c1))
c2 = list(set(c2))
print(len(c1))
print(len(c2))

for z in c1:
    for u in c2:
        if abs(u[0] - z[0]) < 1 and abs(u[1] - z[1]) < 1:
            pass
        else:
            changed_objects_initial.append(u)

changed_objects_initial = list(set(changed_objects_initial))
print(len(changed_objects_initial))

plt.figure()
plt.imshow(z1, cmap='gray')
plt.colorbar()

for i in changed_objects_initial:
    plt.plot(i[0], i[1], 'oc')

plt.show()
