from re import fullmatch

def solution(my_string):
  assert 1 <= len(my_string) <= 110
  assert fullmatch(r"[a-zA-Z\s]+", my_string)

  return "".join(dict.fromkeys(my_string))