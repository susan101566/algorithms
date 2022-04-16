from collections import defaultdict

f = open('input.txt', 'r')
m = []
result = 0
for line in f.read().strip().split('\n'):
    m.append(map(int, list(line)))
h = len(m)
w = len(m[0])

def nei(i, j):
    r = []
    for x in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if x[0] >= 0 and x[0] < h and x[1] >= 0 and x[1] < w:
            r.append(x)
    return r

mins = set()
for i in xrange(len(m)):
    for j in xrange(len(m[0])):
        v = m[i][j]
        is_min = True
        for n in nei(i, j):
            if m[n[0]][n[1]] <= v:
                is_min = False
                break
        if is_min:
            mins.add((i, j))

def get_basin(m, bi, bj):
    bfs = [(bi, bj)]
    result = 0
    while len(bfs) > 0:
        i, j = bfs.pop(0)
        if m[i][j] == 9 or m[i][j] == None:
            continue
        m[i][j] = None
        result += 1
        for q in nei(i, j):
            bfs.append(q)
    print '-----------'
    print bi, bj
    print result
    return result
    
result = []
for (i, j) in mins:
    result.append(get_basin(m, i, j))
result = sorted(result)[-3:]
v = 1
for r in result:
    v *= r
print v

