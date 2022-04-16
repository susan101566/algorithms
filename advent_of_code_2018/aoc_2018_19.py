import re
import operator as op
from collections import defaultdict

def do_reg(f, regs, a, b, c):
    regs[c] = f(regs[a], regs[b])

def do_imm(f, regs, a, b, c):
    regs[c] = f(regs[a], b)

def sreg(regs, c, v):
    regs[c] = v

fs = {
    'addr' : lambda regs, a, b, c: do_reg(op.add, regs, a, b, c),
    'addi' : lambda regs, a, b, c: do_imm(op.add, regs, a, b, c),
    'mulr' : lambda regs, a, b, c: do_reg(op.mul, regs, a, b, c),
    'muli' : lambda regs, a, b, c: do_imm(op.mul, regs, a, b, c),
    'banr' : lambda regs, a, b, c: do_reg(op.and_, regs, a, b, c),
    'bani' : lambda regs, a, b, c: do_imm(op.and_, regs, a, b, c),
    'borr' : lambda regs, a, b, c: do_reg(op.or_, regs, a, b, c),
    'bori' : lambda regs, a, b, c: do_imm(op.or_, regs, a, b, c),
    'setr' : lambda regs, a, b, c: sreg(regs, c, regs[a]),
    'seti' : lambda regs, a, b, c: sreg(regs, c, a),
    'gtir' : lambda regs, a, b, c: sreg(regs, c, 1 if a > regs[b] else 0),
    'gtri' : lambda regs, a, b, c: sreg(regs, c, 1 if regs[a] > b else  0),
    'gtrr' : lambda regs, a, b, c: sreg(regs, c, 1 if regs[a] > regs[b] else 0),
    'eqir' : lambda regs, a, b, c: sreg(regs, c, 1 if a == regs[b] else 0),
    'eqri' : lambda regs, a, b, c: sreg(regs, c, 1 if regs[a] == b else 0),
    'eqrr' : lambda regs, a, b, c: sreg(regs, c, 1 if regs[a] == regs[b] else 0)
}

f = open('input.txt', 'r')
lines = f.read().strip().split('\n')
ip_reg = int(lines[0].split(' ')[1])
program = []
ln = 0
for line in lines[1:]:
    o, a, b, c = line.split(' ')
    a, b, c = map(int, [a,b,c])
    program.append([o, a, b, c])
    ln += 1

regs = [0] * 6
regs[0] = 1
ip = regs[ip_reg] # start at 0
reps = 10000
while ip >= 0 and ip < len(program) and reps > 0:
    pl = str(ip) + ' [' + ','.join(map(str, regs)) + ']'
    regs[ip_reg] = ip
    instr = program[ip]
    pl += ' '.join(map(str, instr))
    fn = fs[instr[0]]
    fn(regs, instr[1], instr[2], instr[3])
    ip = regs[ip_reg] 
    ip += 1
    reps -= 1
    print pl, regs

