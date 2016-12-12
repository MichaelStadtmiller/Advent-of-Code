import csv
def filetolist(myfile):
    mylist = []
    with open(myfile) as f:
            lines = csv.reader(f,delimiter=',')
            for myinput in lines:
                    for i in myinput:
                            mylist.append(i.strip())
                            #move(coord,str(i.strip()[:1]),int(i.strip()[1:]))
                            #print coord
    return mylist
