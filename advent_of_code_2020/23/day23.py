# https://adventofcode.com/2020/day/23
# Given a circular sequence, with one subsequence transplanted every round, how do you do this efficiently? Do not hate linked list ever again.
cups_sample = map(int, list('389125467'))
cups = map(int, list('963275481'))
for i in xrange(10, 10**6+1):
    cups.append(i)

nextcups = [None] * (len(cups) + 1)
for i, c in enumerate(cups):
    nextcups[c] = cups[(i+1) % len(cups)]
cv = cups[0]
for i in xrange(10 * (10**6)):
    aim = cv - 1
    if aim == 0:
        aim = len(cups)
    v = cv
    n1 = None
    n3 = None
    next3 = set()
    for i in xrange(4):
        v = nextcups[v]
        if i != 3:
            next3.add(v)
        if i == 0:
            n1 = v
        if i == 2:
            n3 = v
    while aim in next3:
        aim = (aim - 1) 
        if aim == 0:
            aim = len(cups)

    nextcups[cv] = v
    nextcups[n3] = nextcups[aim]
    nextcups[aim] = n1
    cv = v

print nextcups[1] * nextcups[nextcups[1]]

