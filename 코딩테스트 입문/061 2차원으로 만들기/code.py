def solution(num_list, n):
  assert len(num_list) % n == 0
  assert 2 <= n < len(num_list) <= 150

  return [num_list[i:i+n] for i in range(0, len(num_list), n)]