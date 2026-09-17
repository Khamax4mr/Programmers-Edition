def solution(box, n):
  assert 1 <= n <= 50
  assert len(box) == 3
  assert 1 <= box[0] <= 100 and 1 <= box[1] <= 100 and 1 <= box[2] <= 100

  return (box[0]//n) * (box[1]//n) * (box[2]//n)