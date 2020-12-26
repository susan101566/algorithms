# https://adventofcode.com/2020/day/3
# There is a pattern (input) that is repeated to the right many times. For each of the slopes, determine the number of trees you'd hit. 

f = open('input.txt', 'r')
pattern = f.read().strip().splitlines()
width = len(pattern[0])
height = len(pattern)

tests = [(1, 1), (3,1), (5,1), (7,1),(1,2)]
ans = 1
for x, y in tests:
    row = 0
    col = 0
    result = 0
    while row < height:
        col += x
        row += y
        if row >= height:
            break
        c = pattern[row][col % width]
        if c == '#':
            result += 1
    print result
    ans *= result
    
print ans

