def solution(my_string, k):
  assert 1 <= len(my_string) <= 200
  assert my_string.islower()
  assert 1 <= k <= 100

  return my_string * k