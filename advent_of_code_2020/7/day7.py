# https://adventofcode.com/2020/day/7
# each bag contains many other bags. How many bags will you end up with starting from 'gold bag'

import parse
from collections import defaultdict

# f = open('input.txt', 'r')
f = open('input.txt', 'r')
d = defaultdict(list)
for parent, children in map(lambda x: x.replace("bags", "bag").split("bag contain"), f.read().strip().split('\n')):
    children = map(lambda x: x.strip(), children.replace("bags", "bag").replace(",", " ").replace(".", " ").split("bag"))
    for child in children:
        if child != '':
            v = parse.parse("{:d} {}", child)
            if v:
                num, color = v.fixed
                d[parent.strip()].append((color.strip(), num))
                
print d
def calculate(c, multiplier):
    cc = 0
    for t, n in d[c]:
        cc += n 
        cc += calculate(t, n)
    return cc * multiplier

print calculate('shiny gold', 1)


