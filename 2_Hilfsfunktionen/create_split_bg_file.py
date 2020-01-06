# Creates "background-file" for Haar Cascade Training to locate background images.
# it also creates three shorter "backgound-file" for the "opencv_createsamples" function.
# AV-Programmieren, Medientechnik, Wintersemester 2019/2020, Julian Lopes Hinz & Lina Tiedemann.

import urllib.request
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