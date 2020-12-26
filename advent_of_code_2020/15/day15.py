# https://adventofcode.com/2020/day/15
# players take turn saying numbers, with some rule. Simulate many times.
from collections import defaultdict
numbers = [6,4,12,1,20,0,16]
ndumbers = [0, 3, 6]

last = None
spoken = defaultdict(list)
for i in xrange(30000000):
    if i < len(numbers):
        last = numbers[i]
        spoken[last].append(i)
        spoken[last] = spoken[last][-3:]
        print last
        continue
    if len(spoken[last]) == 1:
        v = 0
    else:
        v = spoken[last][-1] - spoken[last][-2]
    last = v
    spoken[last].append(i)
    spoken[last] = spoken[last][-3:]
print last

