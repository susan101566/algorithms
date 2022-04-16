f = open('input.txt', 'r')
array = map(int, f.read().strip().split('\n'))

prev = 10**9
result = 0
count = 0
for i in xrange(2, len(array)):
    result = 0
    for j in xrange(3):
        result += array[i-j]
    if result > prev:
        count += 1
    prev = result

print count


