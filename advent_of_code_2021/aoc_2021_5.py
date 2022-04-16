from collections import defaultdict

board = defaultdict(int)
f = open('input.txt', 'r')
lines = f.read().strip().split('\n')
for line in lines:
    fr, to = line.split(' -> ')
    x1, y1 = map(int, fr.split(','))
    x2, y2 = map(int, to.split(','))
    d = (x2 - x1, y2 - y1)
    d = map(lambda x: x/abs(x) if x != 0 else 0, d)
    x, y = x1, y1
    while not (x == x2 and y == y2):
        board[(x, y)] += 1
        x += d[0]
        y += d[1]
    board[(x, y)] += 1

count = 0
for k, v in board.iteritems():
    if v >= 2:
        count += 1
print count

