def solution(arr):
  assert 1 <= len(arr) <= 200
  assert all(word.islower() and len(word) == 1 for word in arr)

  return "".join(arr)