# https://adventofcode.com/2020/day/4
# validate which passports have valid fields according to some rules.

f = open('input.txt', 'r')
lines = f.read().strip().splitlines()

d = {
        "byr": True,
        "iyr": True,
        "eyr": True,
        "hgt": True,
        "hcl": True,
        "ecl": True,
        "pid": True,
        "cid": True,
}

valid = 0
i = 0
while i < len(lines):
    passport = {}
    while i < len(lines) and lines[i].strip() != '':
        fields = lines[i].strip().split(' ')
        for line in fields:
            k, v = line.split(':')
            passport[k] = v
        i += 1
    i += 1
    seen = False
    count = 0
    for k, v in passport.iteritems():
        print k, v
        print count
        if k == 'byr':
            if len(v) != 4:
                continue
            if 1920 <= int(v) <= 2002:
                count += 1
        elif k == 'iyr':
            if len(v) != 4:
                continue
            if int(v) >= 2010 and int(v) <= 2020:
                count += 1
        elif k == 'eyr':
            if len(v) != 4:
                continue
            if int(v) >= 2020 and int(v) <= 2030:
                count += 1
        elif k == 'hgt':
            if v[-2:] == 'cm':
                rv = int(v[:-2])
                if 150 <= rv <= 193:
                    count += 1
            if v[-2:] == 'in':
                rv = int(v[:-2])
                if 59 <= rv <= 76:
                    count += 1
        elif k == 'hcl':
            if v[0] == '#' and len(v[1:]) == 6:
                for c in v[1:]:
                    if not ('0' <= c <= '9' or 'a' <= c <= 'f'):
                        continue
                count += 1
        elif k == 'ecl':
            if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                count += 1
        elif k == 'pid':
            try:
                if len(v) == 9:
                    q = int(v)
                    count += 1
            except:
                continue
        elif k == 'cid':
            count += 1
            seen = True
        else:
            print 'error', k
    if count == len(d) or (count == len(d) - 1 and not seen):
        valid += 1

print valid

