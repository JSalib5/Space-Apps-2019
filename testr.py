import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


a = cv.imread(r"C:\Users\adity\OneDrive\Desktop\NasaSpaceApps\ng1.png")
b = cv.imread(r"C:\Users\adity\OneDrive\Desktop\NasaSpaceApps\ng.png")


c = a-b
plt.figure()
plt.imshow(c, cmap='gray')
plt.colorbar()
plt.show()