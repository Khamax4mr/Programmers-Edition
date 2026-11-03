def solution(my_string, index_list):
  assert 1 <= len(my_string) <= 1000
  assert my_string.islower()
  assert 1 <= len(index_list) <= 1000
  assert all(0 <= n < len(my_string) for n in index_list)

  return "".join(my_string[i] for i in index_list)