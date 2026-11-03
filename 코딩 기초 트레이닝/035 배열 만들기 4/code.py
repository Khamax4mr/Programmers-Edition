def solution(arr):
  assert 1 <= len(arr) <= 100000
  assert all(1 <= n <= 100000 for n in arr)

  stk = []
  while arr:
    min_n = min(arr)
    stk.append(min_n)
    arr = arr[len(arr)-arr[::-1].index(min_n):]

  return stk