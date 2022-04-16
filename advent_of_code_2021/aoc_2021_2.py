f = open('input.txt', 'r')
d = 0
x = 0
a = 0

for line in f.read().strip().split('\n'):
    c, i = line.split(' ')
    i = int(i)
    if c == 'down':
        a += i
    elif c == 'up':
        a -= i
    elif c == 'forward':
        x += i
        d += a * i

print d * x

