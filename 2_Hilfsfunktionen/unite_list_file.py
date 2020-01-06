# This script unites all info-lists into one file. These are necessary to indicate on
# which coorinates etc. gestures are placed within a positive image.
# AV-Programmieren, Medientechnik, Wintersemester 2019/2020, Julian Lopes Hinz & Lina Tiedemann.

filenames = ['./info/info1.lst', './info/info2.lst','./info/info3.lst', './info/info4.lst','./info/info5.lst', './info/info6.lst']

with open('info/info.lst', 'a') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())