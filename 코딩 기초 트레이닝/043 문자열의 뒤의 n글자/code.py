def solution(my_string, n):
  assert my_string.isalnum()
  assert 1 <= n <= len(my_string) <= 1000

  return my_string[-n:]