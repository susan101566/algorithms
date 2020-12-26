# https://adventofcode.com/2020/day/25
# Find the power of 7 mod 20201227 that matches two keys. Then use the power on the two numbers. Merry Christmas :)
from collections import defaultdict
import copy
import math

key1 = 9093927
key2 = 11001876

#key1 = 5764801
#key2 = 17807724

def transform(v, ls):
    c = 1
    for i in xrange(ls):
        c = (v * c) % 20201227
    return c

v = 1
ls1 = 0
ls2 = 0
for i in xrange(1, 10**9):
    v = (v * 7) % 20201227
    if v == key1:
        ls1 = i
        break

v = 1
for i in xrange(1, 10**9):
    v = (v * 7) % 20201227
    if v == key2:
        ls2 = i
        break

print ls1, ls2
print key1, transform(key1, ls2)
print key2, transform(key2, ls1)

