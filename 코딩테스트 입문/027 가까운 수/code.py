def solution(array, n):
  assert 1 <= n <= 100
  assert 1 <= len(array) <= 100
  assert all(1 <= e <= 100 for e in array)

  return sorted([(abs(i - n), i) for i in array])[0][1]