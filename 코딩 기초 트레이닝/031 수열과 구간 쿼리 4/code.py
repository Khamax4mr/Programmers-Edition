def solution(arr, queries):
  assert 1 <= len(arr) <= 1000
  assert all(0 <= n <= 1000000 for n in arr)
  assert 1 <= len(queries) <= 1000
  assert all(0 <= s <= e < len(arr) for s, e, _ in queries)

  return [arr[i] + sum(s <= i <= e and i % k == 0 for s, e, k in queries) for i in range(len(arr))] 