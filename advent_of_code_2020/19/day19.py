# https://adventofcode.com/2020/day/19
# string matching against rules that refer each other. How many strings match rule 0? Realized that each rule consists of at most 3 sub parts. DP each part.
from collections import defaultdict

f = open('input.txt', 'r')
rules, lines = f.read().strip().split('\n\n')

d = {}
for rule in rules.split('\n'):
    left, right = rule.split(": ")
    if '"' in right:
        d[left] = right[1]
    else:
        right.split('|')
        rs = []
        for r in right.split('|'):
            rs.append(r.strip().split())
        d[left] = rs

for i, v in d.iteritems():
    print i ,v

def do_match(memo, dic, d, l):
    if d in memo and l in memo[d]:
        return memo[d][l]
    if d not in memo:
        memo[d] = {}
    if len(l) == 0:
        return False
    if isinstance(dic[d], str):
        if dic[d] == l:
            memo[d][l] = True
            return True
        memo[d][l] = False
        return False
    for tup in dic[d]:
        # OR relationship
        if len(tup) == 1:
            if do_match(memo, dic, tup[0], l):
                memo[d][l] = True
                return True
        elif len(tup) == 2:
            for i in xrange(len(l)):
                a = l[:i+1]
                b = l[i+1:]
                left_match = do_match(memo, dic, tup[0], a)
                if not left_match:
                    continue
                right_match = do_match(memo, dic, tup[1], b)
                if right_match:
                    memo[d][l] = True
                    return True
        elif len(tup) == 3:
            for i in xrange(len(l)):
                for j in xrange(i+1, len(l)):
                    a = l[:i+1]
                    b = l[i+1:j+1]
                    c = l[j+1:]
                    left_match = do_match(memo, dic, tup[0], a)
                    if not left_match:
                        continue
                    mid_match = do_match(memo, dic, tup[1], b)
                    if not mid_match:
                        continue
                    right_match = do_match(memo, dic, tup[2], c)
                    if right_match:
                        memo[d][l] = True
                        return True
        else:
            print "length of tuple is not 1 or 2"
    memo[d][l] = False
    return False

result = 0
memo = {}
for line in lines.split('\n'):
    print 'matching', line
    if do_match(memo, d, '0', line):
        print 'yes', line
        result += 1

print result

