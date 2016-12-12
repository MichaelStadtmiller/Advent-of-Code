import csv
from fns import filetolist
def move(c,d,v,h):
        if c[2] == 'N':
                if d == 'R':
					c[1]=c[1]+v
					c[2]='E'
                if d == 'L':
					c[1]=c[1]-v
					c[2]='W'
        elif c[2] == 'E':
                if d == 'R':
					c[0]=c[0]-v
					c[2]='S'
                if d == 'L':
					c[0]=c[0]+v
					c[2]='N'
        elif c[2] == 'S':
                if d == 'R':
					c[1]=c[1]-v
					c[2]='W'
                if d == 'L':
					c[1]=c[1]+v
					c[2]='E'
        elif c[2] == 'W':
                if d == 'R':
					c[0]=c[0]+v
					c[2]='N'
                if d == 'L':
					c[0]=c[0]-v
					c[2]='S'

coord = [0,0,'N']
history = []
myl = filetolist('input_day1.txt')
for i in myl:
        move(coord,str(i.strip()[:1]),int(i.strip()[1:]),history)
 #       print coord

print coord
print coord[0]+coord[1]
