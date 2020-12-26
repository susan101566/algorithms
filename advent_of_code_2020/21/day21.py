# https://adventofcode.com/2020/day/21
# given a food list and its corresponding allergens list, determine which food has which allergen. Similar to day 16, find one match, then next, etc.
from collections import defaultdict
import copy
import math

f = open('input.txt', 'r')
lines = f.read().strip().split('\n')
foods = []
atoi = defaultdict(list)
hasAlgs = {}
for index, line in enumerate(lines):
    left, right = line.split('(contains ')
    ingredients = left.strip().split()
    allergens = right[:-1].replace(',', ' ').split()
    foods.append([allergens, ingredients])
    for al in allergens:
        atoi[al].append(index)
    for ing in ingredients:
        hasAlgs[ing] = False

allergens = []
for a, i in atoi.iteritems():
    allergens.append([a, i])
allergens.sort(key = lambda x: len(x[1]), reverse=True)

matches = {}
for x in xrange(10000):
    newFound = False
    for ing, indices in allergens:
        counts = defaultdict(int)
        for ind in indices:
            for n in foods[ind][1]:
                if hasAlgs[n] == True:
                    continue
                counts[n] += 1
        candidates = []
        for n, v in counts.iteritems():
            if v == len(indices):
                candidates.append(n)
        if len(candidates) == 1:
            hasAlgs[candidates[0]] = True
            matches[candidates[0]] = ing
            newFound = True
    if not newFound:
        break

'''
# part 1
print hasAlgs
print foods
count = 0
for x, ing in foods:
    for i in ing:
        if not hasAlgs[i]:
            print i
            count += 1
print count
'''

tuples = []
for k, v in matches.iteritems():
    tuples.append((v, k))

tuples.sort()
result = []
for t in tuples:
    result.append(t[1])

print ','.join(result)
