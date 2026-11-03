def solution(n):
  assert 1 <= n <= 1000

  collatz = [n]
  while collatz[-1] != 1:
    collatz.append(3*collatz[-1]+1 if collatz[-1] & 1 else collatz[-1]//2)

  return collatz