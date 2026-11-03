def solution(a, b, c):
  assert 1 <= a <= 6
  assert 1 <= b <= 6
  assert 1 <= c <= 6

  res = a + b + c
  res *= (a**2 + b**2 + c**2) if a==b or b==c or c==a else 1
  res *= (a**3 + b**3 + c**3) if a==b==c else 1
  return res