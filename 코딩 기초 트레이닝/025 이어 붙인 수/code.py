def solution(num_list):
  assert 2 <= len(num_list) <= 10
  assert all(1 <= n <= 9 for n in num_list)
  assert len(set(n&1 for n in num_list)) == 2

  temp = ["", ""]
  for n in num_list:
    temp[n&1] += str(n)

  return int(temp[0]) + int(temp[1])