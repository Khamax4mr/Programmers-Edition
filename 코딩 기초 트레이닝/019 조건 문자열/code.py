def solution(ineq, eq, n, m):
  assert 1 <= n <= 100
  assert 1 <= m <= 100

  return int(eval((str(n)+ineq+eq+str(m)).replace("!", "")))