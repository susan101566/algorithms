# https://adventofcode.com/2020/day/9
# bruteforce

f = open('input.txt', 'r')

pre = 25
ns = map(int, f.read().strip().split('\n'))

def all_sums(numbers):
    result = {}
    for i in xrange(len(numbers)):
        for j in xrange(i+1, len(numbers)):
            result[numbers[i]+numbers[j]] = True
    return result

aim = 10884537

for i in xrange(len(ns)):
    for j in xrange(i+1, len(ns)):
        if sum(ns[i:j+1]) == aim:
            y = ns[i:j+1]
            y.sort()
            print y[0] + y[-1]


