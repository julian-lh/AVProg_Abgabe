import cv2
import numpy as np
import glob
import os
import sys
from os.path import basename

imgPath = "./inputV"
imgPathOut = "./neg6"
resizeDimH = 100
resizeDimB = 100
newFileNameBase= ''
counter = 1400
amount = 700      #if all in directory then write 0
digits = 0        #length of number of digits being filled with leading zeros

# Check for images
'''
if len(list(glob.iglob('%s/*.jpg' % imgPath))) == 0:
    print 'Could not find any images in path "%s".' % (imgPath)
    sys.exit(2)
'''
if not os.path.exists(imgPathOut):
    os.makedirs(imgPathOut)

maxNr = counter + amount
for filename in glob.iglob('%s/*.jpg' % imgPath):

    counter += 1

    if counter == (maxNr+1) and amount != 0:
        break

    # Read image
    imgOriginal = cv2.imread(filename)

    # Get shortest imagesize
    size = imgOriginal.shape[0:2]
    sqrSize = np.amin(size)
    #print('kleinste Seite: ',sqrSize)

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

    print("\r\rGecropte Bilder: %i\r" % (counter))
    #print '%s/%s' % (imgPath, imgName)
print('CROPPING BEENDET')


#cv2.imshow("Beispiel", img)

#cv2.waitKey(0) #hält Programmablauf an, bis irgendeine Taste (0) gedrück wird
#cv2.destroyAllWindows() #schließt alle Fenster
