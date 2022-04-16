from collections import defaultdict

f = open('input.txt', 'r')
pos = map(int, f.read().strip().split(','))
least = min(pos)
most = max(pos)

def cost(steps):
    if steps == 0:
        return 0
    return (1 + steps) * steps / 2

best = 10000000000000
for i in xrange(least, most+1):
    cur = 0
    for p in pos:
        cur += cost(abs(p - i))
    if cur < best:
        best = cur

print best


