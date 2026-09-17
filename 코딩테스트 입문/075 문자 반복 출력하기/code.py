def solution(my_string, n):
  assert my_string.isalpha()
  assert 2 <= n <= 10
  assert 2 <= len(my_string) <= 5

  return "".join(s*n for s in my_string)