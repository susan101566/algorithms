# https://adventofcode.com/2020/day/1
# part 1: find the two entries that sum to 2020
# part 2: find the three entries that sum to 2020
# d tracks the seen numbers, s tracks the seen sums of two numbers

d = {}
s = {}
while True:
    try:
        v = int(raw_input())
    except:
        break
    if v in d:
        print 'error'
    d[v] = True

for k1 in d:
    for k2 in d:
        if k1 != k2:
            s[k1+k2] = (k1, k2)

for k in d:
    if 2020 - k in s:
        print k * s[2020-k][0] * s[2020-k][1]
