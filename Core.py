#Core dataprocessing for NeoSSAT
import astropy
from astropy.io import fits
import os
import matplotlib.pyplot as plt
import cv2
import numpy as np

imagedata1 = fits.getdata(r'Images\NEOS_SCI_2019001005526_clean.fits', ext=0)
imagedata2 = fits.getdata(r'Images\NEOS_SCI_2019001005732_clean.fits', ext=0)

out = imagedata1-imagedata2
fits.open('Images\NEOS_SCI_2019001010802_clean.fits')[0].header['TIME-OBS'])

#image_data = cv2.sqrBoxFilter(image_data, -5, (1,1))


#image_data = cv2.equalizeHist(image_data)

plt.figure()
plt.imshow(out, cmap='gray')
plt.colorbar()
plt.show()
"""

entries = os.listdir('Images')
print(entries)
for i in entries:
    print((fits.open('Images/' + i))[0].header['TIME-OBS'])
"""

