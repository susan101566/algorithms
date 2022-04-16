from collections import defaultdict
lines = open('input.txt').read().strip().split('\n')
yard = map(list, lines)

def printer(field):
    for l in field:
        print ''.join(l)

def step(field):
    height = len(field)
    width = len(field[0])
    result = [['.' for _ in xrange(width)] for _ in xrange(height)]
    for i in xrange(height):
        for j in xrange(width):
            # go through neighbors
            ntrees = 0
            nlumber = 0
            for dh in xrange(-1, 2):
                for dw in xrange(-1, 2):
                    ni = i+dh
                    nj = j+dw
                    if dh == 0 and dw == 0:
                        continue
                    if ni >= 0 and ni < height and nj >= 0 and nj < width:
                        ntrees += 1 if field[ni][nj] == '|' else 0
                        nlumber += 1 if field[ni][nj] == '#' else 0
            # rules
            if field[i][j] == '.' and ntrees >= 3:
                result[i][j] = '|'
                continue
            elif field[i][j] == '|' and nlumber >= 3:
                result[i][j] = '#'
                continue
            elif field[i][j] == '#':
                if nlumber >= 1 and ntrees >= 1:
                    result[i][j] = '#'
                else:
                    result[i][j] = '.'
                continue
            else:
                result[i][j] = field[i][j]
    return result

def value(field):
    ntrees = 0
    nlumber = 0
    for i in xrange(len(yard)):
        for j in xrange(len(yard[0])):
            c = yard[i][j]
            if c == '#':
                nlumber +=1 
            elif c == '|':
                ntrees += 1
    return ntrees, nlumber

# figure out the pattern
indices = defaultdict(list)
for i in xrange(1000):
    yard = step(yard)
    v = value(yard)
    indices[v].append(i)

cycle_length = None
for k, v in indices.iteritems():
    if len(v) > 10:
        cycle_length = v[-1] - v[-2]
        break

hit = 10**9 - 1
for k, v in indices.iteritems():
    if len(v) > 10 and (hit-v[-1])%cycle_length == 0:
        print k[0] * k[1]
        break

