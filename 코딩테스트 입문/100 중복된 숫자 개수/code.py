def solution(array, n):
  assert 1 <= len(array) <= 100
  assert all(0 <= a <= 1000 for a in array)
  assert 0 <= n <= 1000

  return array.count(n)