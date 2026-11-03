def solution(arr, queries):
  assert 1 <= len(arr) <= 1000
  assert all(0 <= n <= 1000000 for n in arr)
  assert 1 <= len(queries) <= 1000
  assert all(0 <= s <= e < len(arr) and 0 <= k <= 1000000 for s, e, k in queries)

  ans = []
  for s, e, k in queries:
    cands = [n for n in arr[s:e+1] if n > k]
    ans.append(min(cands) if cands else -1)

  return ans