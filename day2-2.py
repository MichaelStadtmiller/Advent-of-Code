from fns import filelinestolist
def left(pos):
    if pos[1] == 0:
        return pos
    else:
        newpos = (pos[0],pos[1]-1)
        if getval(newpos) =='X':
            return pos
        else:
            return newpos

def right(pos):
    if pos[1] == 4:
        return pos
    else:
        newpos = (pos[0],pos[1]+1)
        if getval(newpos) == 'X':
            return pos
        else:
            return newpos

def up(pos):
    if pos[0] == 0:
        return pos
    else:
        newpos = (pos[0]-1,pos[1])
        if getval(newpos) == 'X':
            return pos
        else:
            return newpos

def down(pos):
    if pos[0] == 4:
        return pos
    else:
        newpos = (pos[0]+1,pos[1])
        if getval(newpos) == 'X':
            return pos
        else:
            return newpos

def findxy(val):
    for l in map:
        if l.find(val) != -1:
            z = (map.index(l), l.find(val))
            return z
    return 0

def getval(coords):
    x = map[coords[0]]
    return x[coords[1]]

mylist = filelinestolist('input_day2.txt')
map = filelinestolist('map.txt')
a = []
pos = (2,0)
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
    a.append(getval(pos))
print(a)
