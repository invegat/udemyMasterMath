#!/home/linuxbrew/.linuxbrew/bin/python3.7

# import math
import os
# import random
# import re
# import sys
import collections

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
  LA = len(alice)
  r = [0] * LA

  ii = 1
  while alice[LA-ii] > scores[0]:
    ii += 1
  ii -= 1

  j = 0
  for i in range(ii):
    r[LA - i - 1]  = 1
    print('LA', LA, 'i', i, 'j', j, 'alice i -1,-2', alice[LA - i - 1], alice[LA - i - 2])
    if alice[LA - i - 1] > alice[LA - i - 2]: 
      j += 1

  # j = -1
#  p = 10**10 # bigger than any score max of 10**9
  # index = 0
  # LS = len(scores)
  scores_ = list(sorted(list(set(scores)),reverse=True))
  print('scores_', scores_)
  LS_ = len(scores_)
  hsh = dict.fromkeys(range(scores_[LS_-1], scores_[0]+1))
  index = 0
  for k in hsh:
    # print('index', index, "scores_[LS_ - index -1]", scores_[LS_ - index - 1])
    if k == scores_[LS_ - index - 1]:
      index += 1
    hsh[k] = LS_ - index + 1

  # print('hsh', hsh)


  # print('scores_[LS_-1]',scores_[LS_-1], 'LS_', LS_)
  li = 0
  while alice[li] < scores_[LS_-1]:
    li += 1


  j = li
  for i in range(li,0,-1):
    r[li - i] = LS_ + 1
    if alice[li] < alice[li - 1]:
      j -= 1


  print('li', li, 'ii', ii, 'r', r)

  for i in  range(li,LA - ii):
    r[i] = hsh[alice[i]]
  
  return r



#9
# 200000
# 30000


r = climbingLeaderboard(scores,alice)
with  open('climbingTheLadder_testResults.txt', "w") as F:
    L = len(r)
    for  i in range(L):
        F.write("%g\n" % (r[i]))


    return [g if g < 38 else (g + 5 - (g % 5) if g % 5 > 2 else g) \
        for g in grades