def solution(n, k):
  assert 0 < n < 1000
  assert n//10 <= k < 1000
  
  return n*12000 + (k - n//10)*2000