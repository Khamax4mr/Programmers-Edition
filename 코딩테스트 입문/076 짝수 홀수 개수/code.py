def solution(num_list):
  assert 1 <= len(num_list) <= 100
  assert all(0 <= n <= 1000 for n in num_list)

  n_odd = sum(n & 1 for n in num_list)
  return [len(num_list)-n_odd, n_odd]