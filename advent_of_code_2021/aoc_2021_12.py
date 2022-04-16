from collections import defaultdict

def isLower(c):
    return c.lower() == c

def times(l, c):
    co = 0
    for i in l:
        if i == c:
            co += 1
    return co

''' part 1
def dfs(graph, paths, sofar, node):
    if node == 'end':
        sofar.append('end')
        paths.append(sofar)
        return 
    if (isLower(node) or node == 'start') and node in sofar:
        return 
    sofar.append(node)
    for n in graph[node]:
        dfs(graph, paths, sofar[:], n)
'''

def dfs(graph, paths, sofar, node, pin):
    if node == 'end':
        sofar.append('end')
        paths.append(sofar)
        return 
    if node in sofar:
        if node == 'start':
            return
        if isLower(node) and node in sofar:
            if node != pin:
                return
            if times(sofar, node) >= 2:
                return
    sofar.append(node)
    for n in graph[node]:
        dfs(graph, paths, sofar[:], n, pin)

f = open('input.txt', 'r')
lines = f.read().strip().split('\n')
graph = defaultdict(list)
sms = set()
for line in lines:
    n1, n2 = line.split('-')
    graph[n1].append(n2)
    graph[n2].append(n1)
    if isLower(n1):
        sms.add(n1)
    if isLower(n2):
        sms.add(n2)
paths = []
for p in sms:
    dfs(graph, paths, [], 'start', p)
    '''
for p in paths:
    print p
    '''
print len(set(map(tuple, paths)))

