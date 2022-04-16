from collections import defaultdict

def decode(words, digits):
    # training
    d = {}
    m = {2: 1, 3: 7, 4: 4, 7: 8}
    for w in words:
        if len(w) in m:
            # d[1] = {c, f}
            d[m[len(w)]] = set(list(w))
    for w in words:
        ls = set(list(w))
        if len(w) == 6:
            # 0, 9
            if (d[8] - ls).issubset(d[1]):
                d[6] = ls
            elif (d[8] - ls).issubset(d[4]):
                d[0] = ls
            else:
                d[9] = ls
        elif len(w) == 5:
            if (d[8] - ls).issubset(d[4]):
                d[2] = ls
            elif d[1].issubset(ls):
                d[3] = ls
            else:
                d[5] = ls
    # decode
    cy = {}
    r = []
    for k, v in d.iteritems():
        cy[''.join(sorted(list(v)))] = k
    for d in digits:
        k1 = ''.join(sorted(d))
        if k1 in cy:
            r.append(str(cy[k1]))
        else:
            print 'not found'
    return int(''.join(r))

f = open('input.txt', 'r')
lines = f.read().strip().split('\n')
r = 0
for line in lines:
    p1, p2 = line.split(' | ')
    r += decode(p1.split(), p2.split())

print r

