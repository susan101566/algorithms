# https://adventofcode.com/2020/day/8
# follow the rules of the computer and keep state
def tr(instructions):
    acc = 0
    line = 0
    seen = set()
    found = False
    while line not in seen:
        seen.add(line)
        if line >= len(instructions):
            found = True
            break
        i, n = instructions[line].split()
        n = int(n)
        if i == "acc":
            acc += n
            line += 1
        elif i == "jmp":
            line += n
        else:
            line += 1
    return found, acc


f = open('input.txt', 'r')
instructions = f.read().strip().split('\n')

for i in xrange(len(instructions)):
    ins, n = instructions[i].split()
    if ins == 'nop':
        copy = instructions[:i] + ['jmp' + ' ' + n ] + instructions[i+1:]
        found, acc = tr(copy)
        if found:
            break
    if ins == 'jmp':
        copy = instructions[:i] + ['nop' + ' ' + n ] + instructions[i+1:]
        found, acc = tr(copy)
        if found:
            break

print acc


