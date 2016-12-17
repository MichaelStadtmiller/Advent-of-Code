import csv
def filetolist(myfile):
    mylist = []
    with open(myfile) as f:
            lines = csv.reader(f,delimiter=',')
            for myinput in lines:
                    for i in myinput:
                            mylist.append(i.strip())
    return mylist

def filelinestolist(myfile):
    mylist = []
    with open(myfile) as f:
        lines = [x.strip('\n') for x in f.readlines()]
        for l in lines:
            mylist.append(l)
    return mylist

