# https://adventofcode.com/2020/day/11
# conway's game of life, chairs edition.
f = open('input.txt', 'r')
seats = map(list, f.read().strip().split('\n'))

def hash(seatss):
    return ''.join(map(lambda x: ''.join(x), seatss))

def p(b):
    for i in b:
        print ''.join(i)

prev = ''
cu = seats

for it in xrange(100000000):
    key = hash(cu)
    if key == prev:
        count = 0
        for row in cu:
            for col in row:
                if col == '#':
                    count += 1
        print count
        break
    prev = key
    height = len(cu)
    width = len(cu[0])
    n = [['' for y in xrange(width)] for x in xrange(height)]
    for r in xrange(height):
        for c in xrange(width):
            # neighbors
            occupied = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue
                    for k in xrange(1, 100000000):
                        if r + k*i >= 0 and r + k*i < height and c + k*j >= 0 and c + k*j < width:
                            if cu[r+k*i][c+k*j] == '#':
                                occupied += 1 
                                break
                            if cu[r+k*i][c+k*j] == 'L':
                                break
                        else:
                            break
            if cu[r][c] == 'L' and occupied == 0:
                n[r][c] = '#'
            elif cu[r][c] == '#' and occupied >= 5:
                n[r][c] = 'L'
            else:
                n[r][c] = cu[r][c]
    cu = n





