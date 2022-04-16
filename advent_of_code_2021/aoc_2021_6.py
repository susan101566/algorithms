from collections import defaultdict

f = open('input.txt', 'r')
fishes = defaultdict(int)
for fish in map(int, f.read().strip().split(',')):
    fishes[fish] += 1

days = 256
for i in xrange(days):
    new_fishes = defaultdict(int)
    for fish, count in fishes.iteritems():
        if fish == 0:
            new_fishes[6] += count
            new_fishes[8] += count
        else:
            new_fishes[fish-1] += count
    fishes = new_fishes

count = 0
for k, v in fishes.iteritems():
    count += v
print count

