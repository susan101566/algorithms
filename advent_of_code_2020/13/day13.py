# https://adventofcode.com/2020/day/13
# This might be my favorite question. Given a bunch of bus schedules that depart with different time cycles find the first time where one departs exactly one hour after the previous one. Chinese remainder theorem I heard is the way to go, but here, we greedily match a prefix of buses. keeping track of the multiplier that maintains the current matched prefix (1, 2, 3...).
'''
f = open('input.txt', 'r')
inputs = f.read().strip().split('\n')
aim = int(inputs[0])
factors = []
mini = 10000000000
bus = -1

for c in inputs[1].split(','):
    if c != 'x':
        f = int(c)
        if aim % f == 0:
            mini = min(0, mini)
            bus = f
            continue
        diff = f - (aim % f)
        print f, diff
        if diff < mini:
            mini = diff
            bus = f

print bus * mini

'''

f = open('input.txt', 'r')
inputs = f.read().strip().split('\n')
factors = []
offset = 0
for c in inputs[1].split(','):
    if c != 'x':
        f = int(c)
        factors.append((f, offset))
    offset += 1

first = factors[0][0]
start = 0
product = 1
for (f, off) in factors:
    linedup = (start % first + off) % f  == 0
    while not linedup:
        start += product
        linedup = (start + off) % f  == 0
    product *= f
print start
