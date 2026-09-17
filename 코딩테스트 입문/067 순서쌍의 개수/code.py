def solution(n):
  assert 1 <= n <= 1000000

  sqrt = int(n**0.5)
  n_pairs = [n % i for i in range(1, sqrt+1)].count(0)*2
  is_duplicated = (sqrt**2 == n)
  return n_pairs - is_duplicated