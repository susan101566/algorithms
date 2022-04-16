import re
import operator as op
from collections import defaultdict

def do_reg(f, regs, a, b, c):
    regs[c] = f(regs[a], regs[b])

def do_imm(f, regs, a, b, c):
    regs[c] = f(regs[a], b)

def sreg(regs, c, v):
    regs[c] = v

addr = lambda regs, a, b, c: do_reg(op.add, regs, a, b, c)
addi = lambda regs, a, b, c: do_imm(op.add, regs, a, b, c)

mulr = lambda regs, a, b, c: do_reg(op.mul, regs, a, b, c)
muli = lambda regs, a, b, c: do_imm(op.mul, regs, a, b, c)

banr = lambda regs, a, b, c: do_reg(op.and_, regs, a, b, c)
bani = lambda regs, a, b, c: do_imm(op.and_, regs, a, b, c)

borr = lambda regs, a, b, c: do_reg(op.or_, regs, a, b, c)
bori = lambda regs, a, b, c: do_imm(op.or_, regs, a, b, c)

setr = lambda regs, a, b, c: sreg(regs, c, regs[a])
seti = lambda regs, a, b, c: sreg(regs, c, a)

gtir = lambda regs, a, b, c: sreg(regs, c, 1 if a > regs[b] else 0)
gtri = lambda regs, a, b, c: sreg(regs, c, 1 if regs[a] > b else  0)
gtrr = lambda regs, a, b, c: sreg(regs, c, 1 if regs[a] > regs[b] else 0)

eqir = lambda regs, a, b, c: sreg(regs, c, 1 if a == regs[b] else 0)
eqri = lambda regs, a, b, c: sreg(regs, c, 1 if regs[a] == b else 0)
eqrr = lambda regs, a, b, c: sreg(regs, c, 1 if regs[a] == regs[b] else 0)

all_ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

# possible matchings
matchings = defaultdict(set)

def matches_3(before, code, after):
    dups = 0
    index = 0
    for op in all_ops:
        btemp = before[:]
        op(btemp, code[1], code[2], code[3])
        if btemp == after:
            dups += 1
            matchings[code[0]].add(index)
        index += 1
    return dups >= 3

f = open('input.txt', 'r')
count = 0
part1, part2 = f.read().strip().split('\n\n\n')
part1arr = part1.split('\n\n')
for item in part1arr:
    l1, l2, l3 = item.strip().split('\n')
    before = map(int, re.match(r'Before:\s+\[(?P<arr>.*)\]', l1).group('arr').split(', '))
    code = map(int, l2.split(' '))
    after = map(int, re.match(r'After:\s+\[(?P<arr>.*)\]', l3).group('arr').split(', '))
    if matches_3(before, code, after):
        count += 1

# part 1
#print count

# part 2
matches = {}
matched = set()
loop = 0
while len(matchings) and loop < 1000:
    next_matchings = {}
    for k, v in matchings.iteritems():
        actual_v = set()
        for vv in v:
            if vv not in matched:
                actual_v.add(vv)
        if len(actual_v) == 1:
            matches[k] = actual_v.pop()
            matched.add(matches[k])
        else:
            next_matchings[k] = actual_v
    matchings = next_matchings
    loop += 1

registers = [0, 0, 0, 0]
program = []
for line in part2.strip().split('\n'):
    program.append(map(int, line.strip().split(' ')))

for line in program:
    all_ops[matches[line[0]]](registers, line[1], line[2], line[3])

print registers

