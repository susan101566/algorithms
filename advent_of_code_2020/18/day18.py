# https://adventofcode.com/2020/day/18
# + and * have opposite precedence than irl. This approach exhausts all ops with higher precedence first then calculates what's left.
f = open('input.txt', 'r')
lines = f.read().strip().split('\n')

def isDone(line):
    last = None
    for i, c in enumerate(line):
        if c == '(':
            last = i
        if c == ')':
            return (last + 1, i)
    return None

def do_part2(line):
    arr = []
    i = 0
    while i < len(line):
        if line[i] == '+':
            arr.append(int(arr.pop()) + int(line[i+1]))
            i += 2
        else:
            arr.append(line[i])
            i += 1
    sofar = int(arr[0])
    for c in arr[1:]:
        if c == '*':
            continue
        sofar *= int(c)
    return sofar

def do_part1(line):
    start = int(line[0])
    op = None
    for v in line[1:]:
        if v in ['*', '+']:
            op = v
        else:
            if op == '+':
                start += int(v)
            elif op == '*':
                start *= int(v)
            else:
                print 'error', op
    return start

def calculate(line):
    v = isDone(line)
    if v == None:
        return do_part2(line)
    i, j = v
    value = do_part2(line[i:j])
    line = line[0:i-1] + [value] + line[j+1:]
    return calculate(line)

result = 0
for line in lines:
    x = []
    for c in line:
        if c == ' ':
            continue
        x.append(c)
    result += calculate(x)
    print result

