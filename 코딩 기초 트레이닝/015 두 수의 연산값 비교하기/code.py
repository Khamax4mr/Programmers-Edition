def solution(a, b):
  assert 1 <= a < 10000
  assert 1 <= b < 10000

  return max(a*10**len(str(b))+b, 2*a*b)