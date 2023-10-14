import cv2
import numpy as np
import dlib
import cv2.aruco as aruco

from aruco_utils import calculate_pixel_mm_ratio
from ipd_image import imageAnalysis
from ipd_video import live_video_analysis
from utils import midpoint
from utils import template_matching
'''
Using template matching to match the credit card in the image

'''



# For Live Video 
# live_video_analysis(75,aruco.DICT_4X4_100)

# For image only
image_path = 'assets/images/test1.jpeg'

print(f"IPD Distance in mm  {imageAnalysis(image_path,75,aruco.DICT_4X4_100)}")
