import cv2
import numpy as np
import dlib
import cv2.aruco as aruco

from ipd_image import imageAnalysis
from ipd_video import live_video_analysis


# For Live Video 
# live_video_analysis(75,aruco.DICT_4X4_100)

# For image only
image_path = 'assets/images/4.jpg'

print(f"IPD Distance in mm  {imageAnalysis(image_path,75,aruco.DICT_4X4_100)}")
