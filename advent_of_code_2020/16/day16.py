# https://adventofcode.com/2020/day/16
# there are some rules for fields, but we don't know how to match them. Part 1 identifies the invaild ones. In part 2, for the valid ones, try to match these rules with fields (same order in every entry). This approach just happens to work. Find one unambiguous match (which happens to exist), then use it to find the next, etc. 
f = open('input.txt', 'r')
sections = f.read().strip().split('\n\n')
rules = sections[0].split('\n')
mine  = map(int, sections[1].split('\n')[1].split(','))
others = sections[2].split('\n')[1:]

# constraints on the numbers
cons = []
for rule in rules:
    r1, r2 = rule.split(': ')[1].split(' or ')
    r1 = map(int, r1.split('-'))
    r2 = map(int, r2.split('-'))
    cons.append((r1, r2))

valid = []
for other in others:
    # 7,3,47,...
    values = map(int, other.split(','))
    isv = True
    for i, v in enumerate(values):
        matched = False
        for con in cons:
            (l1, l2), (l3, l4) = con
            if (v >= l1 and v <= l2) or (v >= l3 and v <= l4):
                matched = True
                break
        # at least one match
        if not matched:
            isv = False 
            break
    # there exists at least one rule that matches every column
    if isv:
        valid.append(values)

from collections import defaultdict
# rule index to column index
m = defaultdict(list)
for i, ((l1, l2), (l3, l4)) in enumerate(cons):
    # for every column index
    for j in xrange(len(valid[0])):
        allWorks = True
        for v in valid:
            if (v[j] >= l1 and v[j] <= l2) or (v[j] >= l3 and v[j] <= l4):
                pass
            else:
                allWorks = False
                break
        if allWorks:
            m[i].append(j)

final = {}
seen = set()
while len(final) < len(m):
    for i, v in m.iteritems():
        count = 0
        notseen = []
        for vi in v:
            if vi not in seen:
                notseen.append(vi)
        if len(notseen) == 1:
            final[i] = notseen[0]
            seen.add(notseen[0])

result = 1
print final
for i,j in final.iteritems():
    if i < 6:
        result *= mine[j]
print result


    
