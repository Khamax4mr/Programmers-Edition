def solution(a, b):
  assert 0 < len(a) == len(b) < 100
  assert a.islower() and b.islower()

  return (b + b).find(a)