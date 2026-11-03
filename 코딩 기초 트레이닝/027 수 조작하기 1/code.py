from re import fullmatch

def solution(n, control):
  assert -100000 <= n <= 100000
  assert 1 <= len(control) <= 100000
  assert fullmatch(r"[wasd]+", control)

  movement = {"w": 1, "s": -1, "d": 10, "a": -10}
  return n + sum(movement[move] for move in control)