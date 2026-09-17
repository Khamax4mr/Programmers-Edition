from re import fullmatch, sub

def solution(my_string):
  assert fullmatch(r"[a-z\s]+", my_string)
  assert 1 <= len(my_string) <= 1000

  return sub(r"[aeiou]", "", my_string).strip()