def solution(my_string):
  assert my_string.islower()
  assert 1 <= len(my_string) <= 100

  return sorted(my_string[i:] for i in range(len(my_string)))