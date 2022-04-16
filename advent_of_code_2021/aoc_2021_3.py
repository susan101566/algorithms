f = open('input.txt', 'r')
bits = f.read().strip().split('\n')
ps = len(bits[0])

''' part 1
gamma = []
epsilon = []

for i in xrange(ps):
    ones = 0
    zeros = 0
    for b in bits:
        ones += (b[i] == '1')
        zeros += (b[i] == '0')
    print ones, zeros
    if ones > zeros:
        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0')
        epsilon.append('1')

gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)

print gamma, epsilon, gamma * epsilon
'''

oxy = bits[:]
co2 = bits[:]
on = 0
cn = 0
for i in xrange(ps):
    ones = 0
    zeros = 0
    for b in oxy:
        ones += (b[i] == '1')
        zeros += (b[i] == '0')
    oxy2 = []
    for b in oxy:
        if ones >= zeros and b[i] == '1':
            oxy2.append(b)
        if zeros > ones and b[i] == '0':
            oxy2.append(b)
    oxy = oxy2
    if len(oxy) == 1:
        on = int(''.join(oxy), 2)
        break

for i in xrange(ps):
    ones = 0
    zeros = 0
    for b in co2:
        ones += (b[i] == '1')
        zeros += (b[i] == '0')
    co22 = []
    for b in co2:
        if ones < zeros and b[i] == '1':
            co22.append(b)
        if zeros <= ones and b[i] == '0':
            co22.append(b)
    co2 = co22
    if len(co22) == 1:
        cn = int(''.join(co2), 2)
        break

print on, cn, on * cn


