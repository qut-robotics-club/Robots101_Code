import cv2
import numpy as np
import imutils

def find_contours(filtered_image):

    #We need to find the contours using the find contours fucntion and the filtered image 
    # (https://www.geeksforgeeks.org/find-and-draw-contours-using-opencv-python)
    contours = None

    #Process the contours using imultis
    # (https://www.programcreek.com/python/example/121989/imutils.grab_contours)
    contours = [] #Replace this with imultis.grab_contours

    contour_exist = (len(contours) != 0) #We need a condition to test if there are contours, we can test to see if the len = 0

    width_px = []

    if(contour_exist):
        for item in contours:
            width_px.append(int(None)) #We need to get the width of an rectangle using the minAreaReact() function (https://theailearner.com/tag/cv2-minarearect/)
    else:
        width_px.append(-1)

    return contours, width_px