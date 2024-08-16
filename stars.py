import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from astropy.stats import SigmaClip
from photutils.background import Background2D,MedianBackground
fits_file=fits.open('stars.fits')
image_data=fits_file[0].data

sigma_clip=SigmaClip(sigma=3.0)
bkg_estimator=MedianBackground()

bkg=Background2D(image_data,(50,50),filter_size=(3,3),sigma_clip=sigma_clip,bkg_estimator=bkg_estimator)
#bayad az tasvir asli bkg.background ra hazf kard:

final_data=image_data-bkg.background 
#segmentation:

threshold=1.5*bkg.background_rms
from photutils.segmentation import make_2dgaussian_kernel
from astropy.convolution import convolve
kernel=make_2dgaussian_kernel(3.0,size=5) #3fwhm
convolved_data=convolve(final_data,kernel)
from photutils.segmentation import detect_sources
seg_map=detect_sources(convolved_data,threshold,npixels=10)

#deblending:
from photutils.segmentation import deblend_sources
seg_bend=deblend_sources(convolved_data,seg_map,npixels=10,nlevels=32,contrast=0.001)
#creating catalog of detected source
from photutils.segmentation import SourceCatalog
catalog=SourceCatalog(image_data,seg_bend,convolved_data=convolved_data)
table_prop=catalog.to_table()
print(table_prop)