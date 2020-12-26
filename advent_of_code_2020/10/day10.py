# https://adventofcode.com/2020/day/10
# every number need to be at most 3 away from another number. How many ways are there to arrange a sequence using all numbers? Just try all, using dp.
f = open('input.txt', 'r')
ns = map(int, f.read().strip().split('\n'))
ns.sort()
last = ns[-1] + 3

seen = {}

def dp(ns, index, v):
    if (index, v) in seen:
        return seen[(index,v)]
    if index >= len(ns):
        if last - v <= 3:
            seen[(index, v)] = 1
            return 1
        else:
            seen[(index, v)] = 0
            return 0
    ways = 0
    if ns[index] - v <= 3:
        ways += dp(ns, index+1, ns[index])
        ways += dp(ns, index+1, v)
        seen[(index, v)] = ways
        return ways
    seen[(index, v)] = 0
    return 0

print dp(ns, 0, 0)

