def is_c(x):
    return x != '.' and x != '#'

def printer(game, sp, r):
    print '------------ Round ', r
    for l in game:
        pl = ''.join(map(lambda x: sp[x][0] if is_c(x) else x, l))
        pl += ''.join(map(lambda x: ' ' + str(sp[x][0]) + '(' + str(sp[x][1]) + ')'  if is_c(x) else '', l))
        print pl

f = open('input.txt', 'r')
board = map(list, f.read().strip().split('\n'))
h = len(board)
w = len(board[0])

attack = 3
health = 200
sprites = {}
counter = 0
targets_for_e = []
targets_for_g = []
for i in xrange(h):
    for j in xrange(w):
        c = board[i][j]
        if is_c(c):
            sprites[counter] = [c, health]
            board[i][j] = counter
            counter += 1

def neighbors(i, j):
    global h, w
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    r = []
    for (dx, dy) in dirs:
        if i+dx >= 0 and  i+dx < h and j + dy >= 0 and j+dy < w:
            r.append((i+dx, j+dy))
    return r

def update_targets(game, sp):
    global targets_for_e, targets_for_g, w, h
    targets_for_e = []
    targets_for_g = []
    for i in xrange(h):
        for j in xrange(w):
            n = game[i][j]
            if is_c(n):
                c = sp[n][0]
                t = targets_for_g if c == 'E' else targets_for_e
                for (ni, nj) in neighbors(i, j):
                    if game[ni][nj] == '.':
                        t.append((ni, nj))

def move(game, sp, i, j):
    cid = game[i][j]
    c, health = sp[cid]
    targets = targets_for_e if c == 'E' else targets_for_g
    queue = map(lambda (x, y): (x, y, x, y), neighbors(i, j))
    seen = []
    found = None
    while len(queue):
        fromx, fromy, x, y = queue.pop(0)
        if game[x][y] != '.' or (x, y) in seen:
            continue
        if (x, y) in targets:
            found = (fromx, fromy)
            break
        seen.append((x, y))
        for (ni, nj) in neighbors(x, y):
            queue.append((fromx, fromy, ni, nj))
    if found:
        return (i, j, found[0], found[1], cid)
    return None

def do_attack(game, sp, i, j):
    cid = game[i][j]
    cc, ch = sp[cid]
    ns = neighbors(i, j)
    to_attack = None
    for (ci, cj) in ns:
        if is_c(game[ci][cj]):
            nc, nh = sp[game[ci][cj]]
            if cc != nc and (to_attack == None or nh < to_attack[1]):
                to_attack = ((ci, cj), nh)
    if to_attack != None:
        ((ci, cj), nh) = to_attack
        enemy = game[ci][cj]
        e, eh = sp[enemy]
        if eh <= attack:
            del sp[enemy]
            game[ci][cj] = '.'
        else:
            sp[enemy] = [e, eh - attack]
        return True
    return False
    
def step(game, sp):
    already_moved = set()
    for i in xrange(h):
        for j in xrange(w):
            cid = game[i][j]
            if not is_c(cid):
                continue
            if cid in already_moved:
                continue
            update_targets(game, sp)
            already_moved.add(cid)
            # check for attack
            if do_attack(game, sp, i, j):
                continue
            # check for move
            r = move(game, sp, i, j)
            if r:
                (i, j, toi, toj, cid) = r
                game[i][j] = '.'
                game[toi][toj] = cid
                do_attack(game, sp, toi, toj)

def count_c(game, sp):
    count_e = 0
    count_g = 0
    for row in game:
        for ch in row:
            if is_c(ch):
                if sp[ch][0] == 'E':
                    count_e += 1
                else:
                    count_g += 1
    return count_e, count_g

#printer(board, sprites, 0)
for i in xrange(100):
    step(board, sprites)
    printer(board, sprites, i+1)
    ce, cg = count_c(board, sprites)
    if ce == 0 or cg == 0:
        print 'Done!!'
        s = 0
        for k, v in sprites.iteritems():
            s += v[1]
        print i
        print s
        print i * s
        break

