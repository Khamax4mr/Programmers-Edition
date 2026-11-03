def solution(arr, queries):
  assert 1 <= len(arr) <= 1000
  assert all(0 <= n <= 1000000 for n in arr)
  assert 1 <= len(queries) <= 1000
  assert all(0 <= i < j < len(arr) for i, j in queries)

  for i, j in queries:
    arr[i], arr[j] = arr[j], arr[i]

  return arr