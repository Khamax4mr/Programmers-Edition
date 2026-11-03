from re import fullmatch

def solution(code):
  assert 1 <= len(code) <= 100000
  assert fullmatch(r"[a-z1]+", code)

  return "".join(code.split("1"))[::2] or "EMPTY"