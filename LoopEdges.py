import numpy as np
import matplotlib.pyplot as plt
%matplotlib notebook
import astropy.utils.data
import astropy.io.fits
import ftplib
import re

def get_images(year, day):
    # downloads all images for a given day
    # reference:
    # https://learn.astropy.org/rst-tutorials/FITS-images.html
    ROOT_URL = 'ftp.asc-csa.gc.ca'
    WORKING_DIR = '/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/{}/{}/'.format(year, day)
    ftp = ftplib.FTP(ROOT_URL)
    ftp.login()
    ftp.cwd(WORKING_DIR)
    images = {}
    # hdu_list = []
    for filename in ftp.nlst():
        # if 'clean' in filename:
        # if 'cor' in filename:
        if 'cord' in filename:
            # print(filename)
            image_file = astropy.utils.data.download_file(
                'ftp://{}{}{}'.format(ROOT_URL, WORKING_DIR, filename),
                cache=True)
            hdu_list = astropy.io.fits.open(image_file)
            hdu_list.info()
            type(hdu_list)
            image_data = hdu_list[0].data
            print(type(image_data))
            print(image_data.shape)
            hdu_list.close()
            # image_data = astropy.io.fits.getdata(image_file)
            # images[re.search('NEOS_SCI_(.+?)_clean.fits', filename).group(1)] = image_data
            # images[re.search('NEOS_SCI_(.+?)_cor.fits', filename).group(1)] = image_data
            images[re.search('NEOS_SCI_(.+?)_cord.fits', filename).group(1)] = image_data
    ftp.quit()
    return images, hdu_list

    images, hdu_list = get_images('2019', '128')

    data = fits.getdata(r'comet/NEOS_SCI_2015347150900_clean.fits   x', ext=0)






