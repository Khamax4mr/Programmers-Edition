from math import ceil

def solution(n):
  assert 1 <= n <= 100

  return ceil(n/2)**2 if n&1 else int(n*(n+1)*(n+2)/6)