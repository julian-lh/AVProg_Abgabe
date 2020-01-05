import urllib.request
import cv2
import numpy as np
import os

cnt = 0
while cnt < 700:
    cnt +=1
    line = 'neg4/'+str(cnt)+'.jpg\n'
    with open('bg4.txt','a') as f:
        f.write(line)

while cnt < 1400:
    cnt +=1
    line = 'neg5/'+str(cnt)+'.jpg\n'
    with open('bg5.txt','a') as f:
        f.write(line)

while cnt < 2100:
    cnt +=1
    line = 'neg6/'+str(cnt)+'.jpg\n'
    with open('bg6.txt','a') as f:
        f.write(line)

cnt = 0
while cnt < 2100:
    cnt +=1
    line = 'neg/'+str(cnt)+'.jpg\n'
    with open('bg.txt','a') as f:
        f.write(line)