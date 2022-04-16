from collections import defaultdict

f = open('input.txt', 'r')

sd = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
        }
sd2 = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
        }
os = list('[({<')
cs = list('])}>')

def score(line):
    sofar = []
    for c in line:
        if c in os:
            sofar.append(c)
        else:
            expected = cs[os.index(sofar[-1])]
            if c == expected:
                sofar.pop()
            else:
                return (True, sd[c])
    return (False, sofar)

lines = f.read().strip().split('\n')
ss = []
for l in lines:
    v = score(l)
    if v[0]:
        continue
    _, sofar = v
    s = 0
    for c in sofar[::-1]:
        match = cs[os.index(c)]
        s = s * 5 + sd2[match]
    ss.append(s)
ss.sort()
print ss[0], ss[-1]
print ss[len(ss) / 2]

