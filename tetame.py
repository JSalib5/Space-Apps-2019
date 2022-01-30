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


src = cv.imread(r"C:\Users\adity\OneDrive\Desktop\NasaSpaceApps\2019day129-12.PNG")
print(src)
img1 = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
img1 = cv.blur(src, (3, 3))




thresh = 100  # initial threshold

z1, c1 = thresh_callback(thresh, img1)
changed_objects_initial = []
changed_objects_final = []

c1 = list(set(c1))


plt.figure()
plt.imshow(z1, cmap='gray')
plt.colorbar()

for i in c1:
    plt.plot(i[0], i[1], 'oc')

plt.savefig(r'C:\Users\adity\OneDrive\Desktop\NasaSpaceApps\init7.png')
