# Dieses Skript vereint die info.lst Listen zu einer

filenames = ['./info/info1.lst', './info/info2.lst','./info/info3.lst', './info/info4.lst','./info/info5.lst', './info/info6.lst']
with open('info/info.lst', 'a') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())