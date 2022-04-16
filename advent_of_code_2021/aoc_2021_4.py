f = open('input.txt', 'r')
lines = f.read().strip().split('\n\n')

moves = map(int, lines[0].split(','))
boards = []
for line in lines[1:]:
    b = []
    for l in line.strip().split('\n'):
        b.append(map(int, l.strip().split()))
    boards.append(b)

def did_win(board):
    for i in xrange(5):
        nb = 0
        nb1 = 0
        for j in xrange(5):
            if board[j][i] == None:
                nb += 1
            if board[i][j] == None:
                nb1 += 1
            if nb == 5 or nb1 == 5:
                return True
    return False

def su(board):
    r = 0
    for row in board:
        for c in row:
            if c == None:
                r += 0
            else:
                r += c
    return r

def when_win(board, moves):
    b = [row[:] for row in board]
    b = board
    pos = {}
    for i in xrange(5):
        for j in xrange(5):
            pos[board[i][j]] = (i, j)
    which = 0
    for m in moves:
        if m not in pos:
            which += 1
            continue
        i, j = pos[m]
        b[i][j] = None
        if did_win(b):
            return which, su(b) * m
        which += 1
    print 'cannot win'
    return None

maxi = 0
best = None
for board in boards:
    turn, score = when_win(board, moves)
    if turn > maxi:
        maxi = turn
        best = score
        print maxi, best
print best

