# This script crops images into a desired size, converts them into a grayscale image and exports them as jpg image.
# Cropping happens towards the center of the input image.
# AV-Programmieren, Medientechnik, Wintersemester 2019/2020, Julian Lopes Hinz & Lina Tiedemann.
import cv2
import numpy as np
import glob
import os
import sys
from os.path import basename

imgPathIn = "./input"
imgPathOut = "./output"
resizeDimH = 50
resizeDimB = 50
newFileNameBase= "v"
counter = 0
digits = 0        #total length of consecutive number (filled with leading zeros)


# Check for directory
if not os.path.exists(imgPathOut):
    os.makedirs(imgPathOut)

for filename in glob.iglob("%s/*.jpg" % imgPathIn):

    counter += 1
    # Read image
    imgOriginal = cv2.imread(filename)

    # Get shortest imagesize
    size = imgOriginal.shape[0:2]
    sqrSize = np.amin(size)

    # Crop center
    startH = int((size[0]-sqrSize)/2)
    endH = int(((size[0]-sqrSize)/2)+sqrSize)
    startW = int((size[1]-sqrSize)/2)
    endW = int(((size[1]-sqrSize)/2)+sqrSize)
    imgCrop = imgOriginal[startH:endH, startW:endW]

    # Resize
    img = cv2.resize(imgCrop, (resizeDimB, resizeDimH), interpolation = cv2.INTER_AREA)

    # Convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)

    # Write image
    imgIndx = str(counter).zfill(digits)
    imgName = newFileNameBase + imgIndx + ".jpg"
    cv2.imwrite('%s/%s' % (imgPathOut, imgName), img)

    print("\r\rCropped Images: %i\r" % (counter))

print("FINISHED CROPPING")
