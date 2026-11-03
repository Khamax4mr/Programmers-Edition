def solution(num_list):
  assert 1 <= len(num_list) <= 1000
  assert all (0 <= n <= 1000 for n in num_list)

  return num_list[::-1]