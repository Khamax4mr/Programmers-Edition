def solution(board, h, w):
  n = len(board)
  assert 1 <= n <= 7
  assert 0 <= h < n
  assert 0 <= w < n
  assert all(len(line) == n for line in board)
  assert all(1 <= len(board[i][j]) <= 10 and board[i][j].islower() for i in range(h) for j in range(w))

  point = [(h-1, w), (h+1, w), (h, w-1), (h, w+1)]
  color = board[h][w]
  return sum(0 <= dh < n and 0 <= dw < n and board[dh][dw] == color for dh, dw in point)