from collections import defaultdict

f = open('input.txt', 'r')
lines = f.read().strip().split('\n')

initial = list(lines[0])
rules = {}
for pair in lines[2:]:
    f, t = pair.split(' -> ')
    rules[f] = t

# {'ab': {1: {c: 1}, 2: {c:1, d: 1}..., 'bc': ...}
dp = {}

# solve('cv', 10)
# ab
# acb
# adceb
def accum(d1, d2):
    for k, v in d2.iteritems():
        d1[k] = d1[k] + v if k in d1 else v

def solve(pair, steps):
    global dp
    if pair in dp and steps in dp[pair]:
        return dp[pair][steps]
    if steps == 1:
        if pair in rules:
            dp[pair] = { 1: {rules[pair]: 1} }
            return dp[pair][steps]
        return None
    # steps > 1
    if pair not in rules:
        return None

    newc = rules[pair]
    front = pair[0] + newc
    back = newc + pair[1]

    fr = solve(front, steps-1)
    br = solve(back, steps-1)

    dp[pair] = dp[pair] if pair in dp else {}
    dp[pair][steps] = dict(fr) if fr else {}
    accum(dp[pair][steps], br if br else {})
    dp[pair][steps][newc] = dp[pair][steps][newc] + 1 if newc in dp[pair][steps] else 1
    return dp[pair][steps]

prev = {}
for c in initial:
    prev[c] = prev[c] + 1 if c in prev else 1

ts = 40
for i in xrange(len(initial) - 1):
    p = initial[i] + initial[i+1]
    solve(p, ts)
    accum(prev, dp[p][ts])

maxi = None
mini = None
for k, v in prev.iteritems():
    if maxi == None or v > maxi:
        maxi = v
    if mini == None or v < mini:
        mini = v
print maxi - mini

