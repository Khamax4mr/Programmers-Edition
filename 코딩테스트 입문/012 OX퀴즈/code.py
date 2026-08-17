def solution(quiz):
  assert 1 <= len(quiz) <= 10

  result = []
  for expr in quiz:
    tokens = expr.split()
    assert len(tokens) == 5
    
    x, op, y, _, z = tokens
    assert -10000 <= int(x) <= 10000
    assert -10000 <= int(y) <= 10000
    assert -20000 <= int(z) <= 20000
    assert op in {"+", "-"}

    result.append("O" if eval(expr.replace("=", "==")) else "X")

  return result