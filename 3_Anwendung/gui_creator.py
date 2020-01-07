# This Class generates a very simple graphical user interface including a multi-view for
# three different images (mainImg, imgB, imgC) and an overview of possible key inputs.
# It also offers a visual output of detected letters and the audio mute state.
# AV-Programmieren, Medientechnik, Wintersemester 2019/2020, Julian Lopes Hinz & Lina Tiedemann.

import numpy as np
import cv2

class MyGUIClass:

    def __init__(self, sizeX = 600):
        self.sizeX = int(sizeX)
        self.sizeY = int(sizeX*2/3)
        self.sizeYThird = int(self.sizeY/2)

    def getGUIImg(self, mainImg, imgB, imgC, selectedLetter = "empty", mostCommonLetter = "none", audioMuted = False):

        mainImgSmall = cv2.resize(mainImg, (self.sizeY, self.sizeY), interpolation = cv2.INTER_AREA)
        imgBSmall = cv2.resize(imgB, (self.sizeYThird, self.sizeYThird), interpolation = cv2.INTER_AREA)
        imgCSmall = cv2.resize(imgC, (self.sizeYThird, self.sizeYThird), interpolation = cv2.INTER_AREA)

        imgBSmall = cv2.cvtColor(imgBSmall, cv2.COLOR_RGB2BGR)
        #imgCSmall = cv2.cvtColor(imgCSmall, cv2.COLOR_RGB2BGR)
        #mainImgSmall = cv2.cvtColor(mainImgSmall, cv2.COLOR_BGR2RGB)

        # Text output from detection and mute-setting.
        if mostCommonLetter != "none":
            imgBSmall = cv2.putText(imgBSmall, mostCommonLetter.capitalize(), (40,160), cv2.FONT_HERSHEY_DUPLEX, 6, (255,0,255),6)
        if audioMuted:
            imgBSmall = cv2.putText(imgBSmall, "mute", (60,190), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255),2)

        sideImg = np.concatenate((imgBSmall,imgCSmall), axis=0)
        combinedImg = np.concatenate((mainImgSmall, sideImg), axis = 1)

        # Create bottom key input overview.
        label1 = "Selected cascade(s): "+ selectedLetter.upper()
        label2 = "[A] All Cascades  [C] C-Cascade [G] G-Cascade [L] L-Cascade"
        label3 = "[Q] quit  [SPACE] calibrate Mask  [M] mute audio  [V] V-Cascade"
        menuBarBG = np.zeros(shape = (int(self.sizeYThird/3), self.sizeX, 3), dtype = np.uint8)
        menuBar = cv2.putText(menuBarBG, label1, (3,15), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
        menuBar = cv2.putText(menuBarBG, label2, (3,35), cv2.FONT_HERSHEY_DUPLEX, 0.5, (200,200,200))
        menuBar = cv2.putText(menuBarBG, label3, (3,55), cv2.FONT_HERSHEY_DUPLEX, 0.5, (200,200,200))

        outputImg = np.concatenate((combinedImg, menuBar), axis = 0)
        return outputImg