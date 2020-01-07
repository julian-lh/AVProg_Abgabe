# This class detects gestures form sign language within an image and offers tools to mark these.
# It also includes an error correction.
# AV-Programmieren, Medientechnik, Wintersemester 2019/2020, Julian Lopes Hinz & Lina Tiedemann.

import numpy as np
import cv2
import statistics
from collections import Counter

class MyGestureDetection:
    cascades = []
    lastResults = [None]*10
    cascadeDirectories = {
        "c": "Cascades/C-Cascades/c_T4_S13.xml",
        "v": "Cascades/V-Cascades/v_T3_S15.xml",
        "l": "Cascades/L-Cascades/L_T1_S16.xml",
        "g": "Cascades/G-Cascades/g_T1_S22.xml"
    }
    minNeighborsCalibrationOffset = {
        "c": -7,
        "v": 0,
        "l": 8,
        "g": -9
    }
    color = {
        "c": (0,0,255),
        "v": (0,255,0),
        "l": (255,0,0),
        "g": (0,255,255)
    }
    selectedCascade = "all"
    minNeighbors = 10
    minObjSize = 80

    def __init__(self):
        self.loadCascades()

    def loadCascades(self):
        for i in self.cascadeDirectories:
            if i != "" and self.cascadeDirectories[i] != "":
                self.cascades.append([cv2.CascadeClassifier(self.cascadeDirectories[i]), i])
                print("SUCCESS: Letter " + i + " loaded from " + self.cascadeDirectories[i])
            else:
                print("ERROR: invalid Direction: " + i + " from " + self.cascadeDirectories[i])

    def analyzeFrame(self, img):
        letter = self.selectedCascade
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        output = []
        for casc in self.cascades:
            if(casc[1].casefold() == letter.casefold() or letter == "all"):
                outNew = casc[0].detectMultiScale(img, 1.3, (self.minNeighbors+self.minNeighborsCalibrationOffset[casc[1]]), 0, (self.minObjSize,self.minObjSize))
                outNew2 = []
                for (x,y,w,h) in outNew:
                    i = [x,y,w,h,casc[1]]
                    outNew2.append(i)
                output.append(outNew2)
        return output

    def analyzeFrameAndInterpret(self, img):
        letter = self.selectedCascade

        # Shift old results one step forward.
        i = 0
        while i <=8:
            self.lastResults[i] = self.lastResults[i+1]
            i +=1

        newestDetectionData = self.analyzeFrame(img)

        newlyDetectedLetters = []
        for all in newestDetectionData:
            for (x,y,w,h,name) in all:
                newlyDetectedLetters.append(name)

        # Detect most common result within a single frame (intra-frame).
        mostCommonLetterIntra = ()
        if newlyDetectedLetters != []:
            c = Counter(newlyDetectedLetters)
            mostCommonLetterIntra = c.most_common(1)[0]
            self.lastResults[9] = mostCommonLetterIntra[0]
        else:
            self.lastResults[9] = None

        # Detect most common letter within 10 latest frames (inter-frame).
        count = Counter(self.lastResults)
        mostCommonLetterInter = count.most_common(1)[0]
        mostCommonLetter = mostCommonLetterInter[0]

        return newestDetectionData, mostCommonLetter

    def markFrame(self, img, data):
        for all in data:
            for (x,y,w,h,name) in all:
                img = cv2.rectangle(img,(x,y),(x+w,y+h),self.color[name],2)
                img = cv2.putText(img, name, (x,y-3), cv2.FONT_HERSHEY_DUPLEX, 1, self.color[name])
        return img

    def analyzeAndMark(self, img, num = 0):
        data = self.analyzeFrame(img)
        img = self.markFrame(img, data)
        return img

    def setCascade(self, selectedCascadeNew):
        self.selectedCascade = selectedCascadeNew

    def setMinObjectSize(self, size):
        self.minObjSize = size

    def setMinNeighbours(self, value):
        self.minNeighbors = value