from math import comb

def solution(balls, share):
  assert 1 <= balls <= 30
  assert 1 <= share <= 30
  assert share <= balls

  return comb(balls, share)