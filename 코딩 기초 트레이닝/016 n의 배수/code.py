def solution(num, n):
  assert 2 <= num <= 100
  assert 2 <= n <= 9

  return int(not (num % n))