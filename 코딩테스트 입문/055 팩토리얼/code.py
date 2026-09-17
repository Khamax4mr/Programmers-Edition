def solution(n):
  assert 0 < n <= 3628800

  base, res = 1, 1
  while res <= n:
    res *= base
    base += 1
  return base-2