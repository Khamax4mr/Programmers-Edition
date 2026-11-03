def solution(my_string, is_suffix):
  assert my_string.islower() and is_suffix.islower()
  assert 1 <= len(my_string) <= 100
  assert 1 <= len(is_suffix) <= 100

  return int(my_string[-len(is_suffix):] == is_suffix)