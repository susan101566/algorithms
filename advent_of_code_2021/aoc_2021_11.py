from collections import defaultdict

def step(board):
    height = len(board)
    width = len(board[0])
    newb = [[0 for i in xrange(width)] for j in xrange(height)]
    for i in xrange(height):
        for j in xrange(width):
            newb[i][j] = board[i][j] + 1
    flashed = set()
    while True:
        didFlash = False
        for i in xrange(height):
            for j in xrange(width):
                if newb[i][j] <= 9:
                    continue
                elif (i,j) in flashed:
                    continue
                else:
                    flashed.add((i, j))
                    didFlash = True
                for di in xrange(-1, 2):
                    for dj in xrange(-1, 2):
                        if di == 0 and dj == 0: 
                            continue
                        r = i + di
                        c = j + dj
                        if r >= 0 and r < height and c >= 0 and c < width: 
                            newb[r][c] += 1
        if not didFlash:
            break
    for i in xrange(height):
        for j in xrange(width):
            if newb[i][j] > 9:
                newb[i][j] = 0
    return (newb, len(flashed))

f = open('input.txt', 'r')
board = []
for line in f.read().strip().split('\n'):
    board.append(map(int, list(line)))

def printer(board):
    for r in board:
        print r

s = 1
n = len(board) * len(board[0])
while True:
    board, flashed = step(board)
    if flashed == n:
        print s
        break
    s += 1
print s

