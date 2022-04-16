
f = open('input.txt', 'r')
lines = f.read().strip().split('\n')
ori = len(lines)

height = 5 * ori
width = 5 * ori

board = [[0 for _ in xrange(width)] for _ in xrange(height)]
for i, line in enumerate(lines):
    for j, v in enumerate(map(int, line)):
        board[i][j] = v

for mi in xrange(5):
    for mj in xrange(5):
        for i in xrange(ori):
            for j in xrange(ori):
                v = board[i][j]+mi+mj
                board[mi*ori+i][mj*ori+j] = (v-1) % 9 + 1

dp = [[float('inf') for _ in xrange(width)] for _ in xrange(height)]
start = (height - 1, width - 1)
end = (0, 0)
dp[start[0]][start[1]] = board[start[0]][start[1]]

def neighbors(i, j):
    result = []
    for di in xrange(-1, 2):
        for dj in xrange(-1, 2):
            if abs(di + dj) != 1:
                continue
            y = i + di
            x = j + dj
            if x >= 0 and x < width and y >= 0 and y < height:
                result.append((y, x))
    return result

def printer():
    for r in dp:
        print r

queue = [start]
while len(queue) > 0:
    (i, j) = queue.pop(0)
    # populate the cost to each neighbor
    for (ni, nj) in neighbors(i, j):
        nv = board[ni][nj]
        cost = nv + dp[i][j]
        if cost < dp[ni][nj]:
            dp[ni][nj] = cost
            queue.append((ni, nj))

print dp[0][0] - board[0][0]

