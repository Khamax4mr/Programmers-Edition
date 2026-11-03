def solution(a, d, included):
  assert 1 <= a <= 100
  assert 1 <= d <= 100
  assert 1 <= len(included) <= 100
  assert included.count(True) > 0

  return a*included.count(True) + d*sum(i for i, b in enumerate(included) if b)