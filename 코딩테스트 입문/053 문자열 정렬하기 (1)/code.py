from re import fullmatch, sub 

def solution(my_string):
  assert fullmatch(r"[a-z0-9]*[0-9]+[a-z0-9]*", my_string)
  assert 1 <= len(my_string) <= 100

  return sorted(map(int, list(sub(r"[a-zA-Z]", "", my_string).strip())))