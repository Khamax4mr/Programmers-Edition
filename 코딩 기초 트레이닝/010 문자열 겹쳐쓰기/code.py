def solution(my_string, overwrite_string, s):
  assert my_string.isalnum()
  assert overwrite_string.isalnum()
  assert 1 <= len(overwrite_string) <= len(my_string)
  assert 0 <= s <= len(my_string) - len(overwrite_string)

  return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]