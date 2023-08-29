import cv2
import numpy as np


"Accept the current frame of the camera and return the proocessed color mask"
def find_object(frame):
    
    #Upper and Lower HSV bounds for the color mask
    LWR_BOUND = (None,None,None)
    UPR_BOUND = (None,None,None)

    #Use GaussianBlur on the orignal parameter frame (https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html)
    blrd_frame = None

    #Use CvtColor to convert RGB to HSV (https://www.geeksforgeeks.org/python-opencv-cv2-cvtcolor-method)
    hsv_frame = None


    Hue_Overflow = None
    if Hue_Overflow:
        #The Upper and lower bounds of the overlaying HUE
        MAX_HUE = (180, UPR_BOUND[1], UPR_BOUND[2])
        MIN_HUE = (0, LWR_BOUND[1], LWR_BOUND[2])
        
        #Apply the color thresholds to the upper and lower part of our map using the inrange function (Lwr -> Max, Min -> Upr)
        # (https://www.educba.com/opencv-inrange) and the hsv frame
        Lower_Hue = None
        Upper_Hue = None

        binary_image = cv2.bitwise_or(Lower_Hue,Upper_Hue)
    else:
        #Apply the lower and upper bounds to the hsv image using the inrange function (https://www.educba.com/opencv-inrange)
        binary_image = None

    #Threshold value
    KERNAL_THRESHOLD = np.ones((0, 0))
    
    #Apply some filters using the aboove kernal and the binary image. Feel free to experiment with different options 
    # (https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html)
    #The main one you should use is the morphologyEx method
    filtered_image = None

    return [filtered_image, binary_image]