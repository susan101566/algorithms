# https://adventofcode.com/2020/day/2
# follow the rules as outlined.

valid = 0
while True:
    try:
        p1, pswd = raw_input().split(': ')
    except:
        break
    r, c = p1.split(' ')
    r1, r2 = map(int, r.split('-'))
    x = 1 if pswd[r1-1] == c else 0
    y = 1 if pswd[r2-1] == c else 0
    if x + y == 1:
        valid += 1
print valid
