# https://adventofcode.com/2020/day/12
# simulation with directions.
'''
# part 1
f = open('input.txt', 'r')
inputs = map(lambda x: (x[0], int(x[1:])), f.read().strip().split('\n'))

ls = ['N', 'W', 'S', 'E']
rs = ['N', 'E', 'S', 'W']

def turn(lr, d, v, (x, y)):
    if lr == 'L':
        return (ls[(ls.index(d) + (v / 90))%len(ls)], (x, y))
    if lr == 'R':
        return (rs[(rs.index(d) + (v / 90))%len(rs)], (x, y))

ads = {
        'N': lambda (d,v,(x, y)): (d, (x, y+v)),
        'S': lambda (d,v,(x, y)): (d, (x, y-v)),
        'E': lambda (d,v,(x, y)): (d, (x+v, y)),
        'W': lambda (d,v,(x, y)): (d, (x-v, y)),
        'L': lambda (d,v,(x, y)): turn('L',d, v,(x,y)),
        'R': lambda (d,v,(x, y)): turn('R',d, v,(x,y)),
        }

curp = (0, 0)
curd = 'E'
for line in inputs:
    d, v = line
    print d, v
    if d == 'F':
        curd, curp = ads[curd]((curd, v, curp))
    else:
        curd, curp = ads[d]((curd, v, curp))
    print curd, curp
    print abs(curp[0]) + abs(curp[1])
'''

# part 2
f = open('input.txt', 'r')
inputs = map(lambda x: (x[0], int(x[1:])), f.read().strip().split('\n'))

def turn(lr, d, v, (x, y)):
    if lr == 'L':
        return (ls[(ls.index(d) + (v / 90))%len(ls)], (x, y))
    if lr == 'R':
        return (rs[(rs.index(d) + (v / 90))%len(rs)], (x, y))

ads = {
        'N': lambda (v,(x, y)): (x, y+v),
        'S': lambda (v,(x, y)): (x, y-v),
        'E': lambda (v,(x, y)): (x+v, y),
        'W': lambda (v,(x, y)): (x-v, y),

        'L': lambda (v,(x, y)): turn('L',d, v,(x,y)),
        'R': lambda (d,v,(x, y)): turn('R',d, v,(x,y)),
        }

def rotateL(v):
    return (-v[1], v[0])

def rotateR(v):
    return (v[1], -v[0])

wpp = (10, 1)
curp = (0, 0)
for line in inputs:
    d, v = line
    print d, v
    if d == 'F':
        curp = (curp[0] + wpp[0] * v, curp[1] + wpp[1] * v)
    elif d in ['N', 'S', 'E', 'W']:
        wpp = ads[d]((v, wpp))
    elif d == 'L':
        for i in xrange(v / 90):
            wpp = rotateL(wpp)
    elif d == 'R':
        for i in xrange(v / 90):
            wpp = rotateR(wpp)
    print abs(curp[0]) + abs(curp[1])
 
 
