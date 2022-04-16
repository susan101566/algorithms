from collections import defaultdict

f = open('input.txt', 'r')

lines = f.read().strip().split('\n\n')

# '011100111001111'
keys_line = ''.join(lines[0].split('\n'))
keys = map(lambda x: 1 if x == '#' else 0, keys_line)

board_lines = lines[1].split('\n')
size = len(board_lines)

mini = 0
maxi = size

def get_binary(board, ri, ci, loop_index):
  result = ''
  loop_char = 0 if loop_index % 2 == 0 else 1
  for r in xrange(ri-1, ri+2):
    for c in xrange(ci-1, ci+2):
      v = board[(r,c)] if (r,c) in board else loop_char
      result += str(v)
  return int(result, 2)

def printer(board):
  dim = maxi - mini
  b = [['x' for _ in xrange(dim)] for _ in xrange(dim)]
  for (i, j), v in board.iteritems():
    b[i-mini][j-mini] = '.' if v == 0 else '#'
  for r in b:
    print ''.join(r)

board = {}
for i, row in enumerate(board_lines):
  for j, col in enumerate(row):
    board[(i, j)] = 1 if col == '#' else 0

printer(board)

for loop_index in xrange(50):
  new_board = {}
  mini-=1
  maxi+=1
  for i in xrange(mini, maxi):
    for j in xrange(mini, maxi):
      new_board[(i, j)] = keys[get_binary(board, i, j, loop_index)]
  board = new_board
  print '------------', loop_index

count = 0
for k, v in board.iteritems():
  count += v
print count
