def solution(num_list):
  assert 2 <= len(num_list) <= 10
  assert all(1 <= n <= 9 for n in num_list)

  num = -num_list[-2] if num_list[-1] > num_list[-2] else num_list[-1]
  return num_list + [num_list[-1] + num]