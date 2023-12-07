# This script generates binary masks from the Cell Tracking Challenge datasets

import os
import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt
import imageio

# Directories
img_dir = 'train_2D\\Fluo-N2DH-SIM+\\02\\'
mask_dir = 'train_2D\\Fluo-N2DH-SIM+\\02_GT\\SEG\\'
bin_dir = 'test1\\train\\Fluo-N2DH-SIM+\\02_GT\\SEG\\'
# track_dir = 'Fluo-N2DH-SIM+\\02_GT\\TRA\\'

# img_max = np.array([])
# img_min = np.array([])

# Iterate over files in image directory
for file_name in os.listdir(img_dir):
    
    # Time
    time = file_name[1:4]
    
    # Import image
    img_name = img_dir + file_name
    img = tiff.imread(img_name)
    img_arr = np.array(img)
    
    # Segmentation mask
    mask_name = mask_dir + 'man_seg' + time + '.tif'
    mask = tiff.imread(mask_name)
    mask_arr = np.array(mask)
    
    # Binary mask
    bin_arr = (mask_arr > 0)
    bin_arr = bin_arr.astype('uint16')
    
    # # Tracking
    # track_name = track_dir + 'man_track' + time + '.tif'
    # track = tiff.imread(track_name)
    # track_arr = np.array(track)
    
    # # Image and mask plot
    # plt.subplot(1, 2, 1)
    # plt.imshow(img_arr)
    # plt.colorbar()
    # plt.axis('off')
    # plt.clim(0, 1000)
    
    # plt.subplot(1, 2, 2)
    # plt.imshow(mask_arr)
    # plt.colorbar()
    # plt.axis('off')
    # plt.clim(0, 100)
    
    # plt.show()
    
    # # Binary mask plot
    # plt.imshow(bin_arr)
    # plt.axis('off')
    # plt.show()
    
    # Save binary mask
    bin_name = bin_dir + 'man_seg' + time + '.tif'
    imageio.imsave(bin_name, bin_arr)
    
    # # Append max and min value of image
    # img_max = np.append(img_max, [np.max(img_arr)])
    # img_min = np.append(img_min, [np.min(img_arr)])

# print(np.max(img_max))
# print(np.min(img_min))
