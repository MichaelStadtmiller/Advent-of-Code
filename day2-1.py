from fns import filelinestolist
def left(pos):
    if pos in (1,4,7):
        return int(pos)
    else:
        return pos-1

def right(pos):
    if pos in (3,6,9):
        return int(pos)
    else:
        return pos+1

def up(pos):
    if pos in (1,2,3):
        return int(pos)
    else:
        return pos-3

def down(pos):
    if pos in (7,8,9):
        return int(pos)
    else:
        return pos+3

mylist = filelinestolist('i.txt')
a = []
pos = 5
for l in mylist:
    for x in l:
        if x=='L':
            pos = left(pos)
        elif x=='R':
            pos = right(pos)
        elif x=='U':
            pos = up(pos)
        elif x=='D':
            pos = down(pos)
    a.append(pos)
print(a)
