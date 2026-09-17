def solution(hp):
  assert 0 <= hp <= 1000

  dp = [0] * (hp + 1)
  for i in range(1, hp + 1):
    cands = [dp[i-1]]
    if i >= 3: cands.append(dp[i-3])
    if i >= 5: cands.append(dp[i-5])
    dp[i] = min(cands) + 1

  return dp[-1]