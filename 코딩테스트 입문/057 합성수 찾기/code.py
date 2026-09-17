def solution(n):
  assert 1 <= n <= 100

  prime = [False] * (n+1)
  for i in range(2, n+1):
    if prime[i]: continue
    prime[i*2:n+1:i] = [True] * ((n-i)//i)
  return prime.count(True)