# https://adventofcode.com/2020/day/22
# Recursive combat game simulator
from collections import defaultdict
import copy
import math

def subgame(player1, player2):
    p, player = maingame(player1, player2)
    return p

def maingame(player1, player2):
    history = {}
    winner = None
    while len(player1) != 0 and len(player2) != 0:
        kp1 = tuple(player1)
        if kp1 in history and history[kp1] == player2:
            return (1, player1)
        history[tuple(player1)] = player2
        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if len(player1) >= p1 and len(player2) >= p2:
            v = subgame(player1[:p1], player2[:p2])
            if v == 1:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)
        else:
            if p1 > p2:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)
    if len(player1) > 0:
        return (1, player1)
    return (2, player2)

f = open('input.txt', 'r')
p1, p2 = f.read().strip().split('\n\n')
player1 = map(int, p1.split('\n')[1:])
player2 = map(int, p2.split('\n')[1:])
p, player = maingame(player1, player2)
score = 0
for i, c in enumerate(player):
    score += (len(player) - i) * c
print score

