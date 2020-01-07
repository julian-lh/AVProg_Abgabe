# Main script for gesture detection including a GUI and audio output.
# AV-Programmieren, Medientechnik, Wintersemester 2019/2020, Julian Lopes Hinz & Lina Tiedemann.

import numpy as np
import cv2

from detection import MyGestureDetection
from gui_creator import MyGUIClass
from audio_playback import MyAudioClass


cap = cv2.VideoCapture(0)
analyzer = MyGestureDetection()
gui = MyGUIClass(600)
audioPlayer = MyAudioClass()
cv2.namedWindow("Sign Language Translator")


# Slider functions
def sliderMinNeighbours(val):
    analyzer.setMinNeighbours(val)

def sliderMinObjSize(val):
    analyzer.setMinObjectSize(val)

# Slider objects
cv2.createTrackbar("precision", "Sign Language Translator", 0, 20, sliderMinNeighbours)
cv2.setTrackbarPos("precision", "Sign Language Translator", 10)

cv2.createTrackbar("minimal object size", "Sign Language Translator", 2, 200, sliderMinObjSize)
cv2.setTrackbarPos("minimal object size", "Sign Language Translator", 80)


getBGFrame = True
bgFrame = np.zeros(shape = (300, 300, 3), dtype = np.uint8)

# Start main loop
while cap.isOpened():
    ret, frame = cap.read()
    if ret == False:
        break

    # Crop left side of frame.
    frameCropped = frame[:,0:720]
    frameSmall = cv2.resize(frameCropped, (300, 300), interpolation = cv2.INTER_AREA)

    frameSmallBW = cv2.cvtColor(frameSmall, cv2.COLOR_BGR2GRAY)
    if getBGFrame:
        bgFrame = frameSmallBW
        getBGFrame = False

    # Create a difference image, a mask and a masked input image.
    absDiff = cv2.absdiff(frameSmallBW, bgFrame)

    thresh = 15
    ret, mask = cv2.threshold(absDiff, thresh, 255, cv2.THRESH_BINARY)

    maskedFrameSmall = cv2.bitwise_and(frameSmall,frameSmall,mask = mask)

    # Gesture detection
    detectionData, mostCommonLetter = analyzer.analyzeFrameAndInterpret(maskedFrameSmall)
    markedFrame = analyzer.markFrame(frameSmall, detectionData)
    mostCommonLetterChecked = "none"

    if mostCommonLetter != () and mostCommonLetter != None :
        mostCommonLetterChecked = mostCommonLetter
        audioPlayer.playAudio(mostCommonLetterChecked)

    outputImg = gui.getGUIImg(markedFrame, mask, maskedFrameSmall, analyzer.selectedCascade, mostCommonLetterChecked, audioPlayer.isMuted())
    cv2.imshow("Sign Language Translator", outputImg)


    # Interpret key input
    key = cv2.waitKey(30)
    if key != -1:
        print("Key input: "+str(chr(key)))
    if key == 97: #a
        analyzer.setCascade("all")
    elif key == 108: #l
        analyzer.setCascade("l")
    elif key == 118: #v
        analyzer.setCascade("v")
    elif key == 99: #c
        analyzer.setCascade("c")
    elif key == 103: #c
        analyzer.setCascade("g")
    elif key == 109: #m
        audioPlayer.toggleMute()
    elif key == 32: #space
        getBGFrame = True
    elif key == 113: #q
        break


cap.release()
cv2.destroyAllWindows()

