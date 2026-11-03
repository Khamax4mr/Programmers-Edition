from math import ceil

def solution(slice, n):
  assert 2 <= slice <= 10
  assert 1 <= n <= 100

  return ceil(n / slice)