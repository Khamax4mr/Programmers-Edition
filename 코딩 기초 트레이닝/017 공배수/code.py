def solution(number, n, m):
  assert 10 <= number <= 100
  assert 2 <= n <= 10
  assert 2 <= m <= 10

  return int(not (number % n) and not (number % m))