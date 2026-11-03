def solution(intStrs, k, s, l):
  assert 0 <= s <= 100
  assert 1 <= l <= 8
  assert 10**(l-1) <= k < 10**l
  assert 1 <= len(intStrs) <= 10000
  assert s + l <= len(min(intStrs)) <= 120

  cands = map(int, [tok[s:s+l] for tok in intStrs if tok[s:s+l]])
  return [n for n in cands if n > k]