def solution(my_string):
  assert my_string.isalpha()
  assert 1 <= len(my_string) <= 1000

  return my_string.swapcase()