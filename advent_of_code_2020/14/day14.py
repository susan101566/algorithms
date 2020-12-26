# https://adventofcode.com/2020/day/14
# run a mini computer that keeps track of a mask and a value. The mask is intterpreted differently in part 1 and 2. 

import parse

f = open('input.txt', 'r')
inputs = f.read().strip().split('\n')

def app(mask, v):
    s = bin(v)[2:]
    s = '0' * (len(mask) - len(s)) + s
    value = ''
    for i in xrange(len(mask)):
        if mask[i] == 'X':
            value += s[i]
        else:
            value += mask[i]
    return int(value, 2)

def app1(mask, v):
    s = bin(v)[2:]
    s = '0' * (len(mask) - len(s)) + s
    value = ''
    for i in xrange(len(mask)):
        if mask[i] == 'X':
            value += 'X'
        elif mask[i] == '0':
            value += s[i]
        else:
            value += '1'
    return value

def getmasks(mask):
    prefixes = ['']
    for b in mask:
        if b == '0' or b == '1':
            for i in xrange(len(prefixes)):
                prefixes[i] = prefixes[i] + b
        elif b == 'X':
            newp = []
            for p in prefixes:
                newp.append(p + '0')
                newp.append(p + '1')
            prefixes = newp
    return prefixes

memory = {}
masks = []
mask = ''
for line in inputs:
    if line.startswith('mask'):
        mask = line.split(' = ')[1]
    else:
        left, v = line.split(' = ')
        v = int(v)
        mem = int(left[4:-1])
        applied = app1(mask, mem)
        for mx in getmasks(applied):
            memory[mx] = v
        
result = 0
for k, v in memory.iteritems():
    result += v
print result


