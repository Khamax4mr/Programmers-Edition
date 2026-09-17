from re import sub

def solution(polynomial):
  coef = [0, 0]
  tokens = sub(r"(?<!\d)x", "1x", polynomial.replace(" + ", " ")).split()

  for token in tokens:
    n = int(token[:-1] if token.endswith("x") else token)
    assert 0 < n < 100
    coef[token.endswith("x")] += n

  expr = []
  if coef[1]:
    expr.append(("" if coef[1] == 1 else str(coef[1])) + "x")
  if coef[0]:
    expr.append(str(coef[0]))
  return " + ".join(expr)