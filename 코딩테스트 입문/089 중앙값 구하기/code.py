def solution(array):
  assert 0 < len(array) < 100 and len(array) & 1
  assert all(-1000 < n < 1000 for n in array)
  
  return sorted(array)[len(array)//2]