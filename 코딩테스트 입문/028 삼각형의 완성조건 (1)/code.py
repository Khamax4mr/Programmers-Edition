def solution(sides):
  assert len(sides) == 3
  assert all(1 <= n <= 1000 for n in sides)

  a, b, c = sorted(sides)
  return 2 - (a + b > c)