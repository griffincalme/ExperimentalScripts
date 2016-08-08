#griffinc StackOverflow

import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread
from skimage.segmentation import random_walker
from skimage.color import rgb2grey
from scipy.ndimage.filters import gaussian_filter


#change to your directory
image = imread(r'C:\Users\YourNameHere\Downloads\mge1v.png')
grey_image = rgb2grey(image)
blurred = gaussian_filter(grey_image, sigma=6) #play with sigma for blur amount


#Get markers for random walk
def get_markers(grey_array, bottom_thresh, top_thresh):

    markers = np.zeros_like(grey_array)
    markers[grey_array < bottom_thresh] = 1
    markers[grey_array > top_thresh] = 2

    return markers


#perform Random Walker, fills in positive regions
#play with .1 and .15 to set the thresholds for the labels
segmentation = random_walker(blurred, get_markers(blurred, .1, .125), beta=130, mode='bf')


#Plot images
fig, axes = plt.subplots(2, 2, figsize=(12, 11))

ax0, ax1,  ax2, ax3 = axes.ravel()

ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title("Original")

ax1.imshow(grey_image, cmap=plt.cm.gray, interpolation='nearest')
ax1.set_title("Grey")

ax2.imshow(blurred, cmap=plt.cm.gray)
ax2.set_title("Gaussian Blur")

ax3.imshow(segmentation, cmap=plt.cm.gray)
ax3.set_title("Random Walk Segmented")

for ax in axes.ravel():
    ax.axis('off')

fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)


plt.show()
