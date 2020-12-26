# https://adventofcode.com/2020/day/6
# given many groups, each with many people, each person answers many answers, find the number of same answers amongst each group.

from collections import defaultdict
f = open('input.txt', 'r')
groups = f.read().strip().split('\n\n')

counts = 0
for g in groups:
    ans = defaultdict(int)
    fam = g.split('\n')
    for p in fam:
        for c in p:
            ans[c] += 1
    a = len(fam)
    for v in ans.itervalues():
        if v == a:
            counts += 1

print counts

