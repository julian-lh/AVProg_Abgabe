# Creates "background-file" for Haar Cascade Training to locate background images.
# AV-Programmieren, Medientechnik, Wintersemester 2019/2020, Julian Lopes Hinz & Lina Tiedemann.

import urllib.request
import os

cnt = 1400
while cnt < 2100:
    cnt +=1
    line = 'neg3/'+str(cnt)+'.jpg\n'
    with open('bg3.txt','a') as f:
        f.write(line)