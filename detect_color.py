
#taken from https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/, Adrian Rosebrock
import numpy as np
import argparse
import cv2

#constructing argument parse and parsing command line arguments
path = "temp path 2 image"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = path)
args = vars(ap.parse_args())

#loading the image
image = cv2.imread(args["image"])

##defining list of boundaries
#the arrays read backwards and say that RED is from RGB 100, 200 in the first 
#array

#of course, we can adjust these boundaries as we like 
boundaries = [
    ([17, 15, 100], [50, 56, 200]),
    ([86, 31, 4], [220, 88, 50]),
    ([25, 146, 190], [62, 174, 250]),
    ([103, 86, 65], [145, 133, 128])
]


for (lower, upper) in boundaries:
    #creating np arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    #finds the colors within the specified boundaries and aplies the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    #show the images
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitkey(0)

#IMPROVE DOCUMENTATION AND TESTS
