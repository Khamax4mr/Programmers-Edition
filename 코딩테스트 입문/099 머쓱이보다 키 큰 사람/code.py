def solution(array, height):
  assert 1 <= len(array) <= 100
  assert all(1 <= h <= 200 for h in array)
  assert 1 <= height <= 200

  return [h > height for h in array].count(True)