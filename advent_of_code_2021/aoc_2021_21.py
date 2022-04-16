
# part 1
# dice = 1

# for ti in xrange(1000):
#   dt = (dice + 1) * 3
#   pi = ti % 2
#   ps[pi] = (ps[pi] + dt - 1) % 10 + 1
#   ss[pi] += ps[pi]
#   dice += 3

#   if ss[pi] >= 1000:
#     print (ti+1)*3, ss[1-pi]
#     print (ti + 1) * ss[1-pi] * 3
#     break

# part 2
# 0,1,2 is p1's turn
# 3,4,5 is p2's turn
memo = {}
def roll(scores, poss, turn, dice_sum):
  key = (scores[0], scores[1], poss[0], poss[1], turn, dice_sum)
  if key in memo:
    return memo[key]

  pi = 0 if turn in [0,1,2] else 1
  next_turn = (turn + 1) % 6

  ways_to_win = [0, 0]

  # scoring turn
  if turn == 2 or turn == 5:
    for r in [1,2,3]:
      new_sum = dice_sum + r
      new_pos = (poss[pi] + new_sum - 1) % 10 + 1
      if (scores[pi] + new_pos) >= 21:
        ways_to_win[pi] += 1
      else:
        new_scores = list(scores)
        new_scores[pi] += new_pos
        new_poss = list(poss)
        new_poss[pi] = new_pos
        p1wins, p2wins = roll(new_scores, new_poss, next_turn, 0)
        ways_to_win[0] += p1wins
        ways_to_win[1] += p2wins
    memo[key] = ways_to_win
    return ways_to_win

  for r in [1,2,3]:
    p1wins, p2wins = roll(scores, poss, next_turn, dice_sum + r)
    ways_to_win[0] += p1wins
    ways_to_win[1] += p2wins
  memo[key] = ways_to_win
  return ways_to_win

ps = [9, 4]
ss = [0, 0]
print roll(ss, ps, 0, 0)
