from math import prod

def solution(num_list):
  assert 2 <= len(num_list) <= 10
  assert all(1 <= n <= 9 for n in num_list)

  return int(prod(num_list) < sum(num_list)**2)