def solution(dot):
  assert len(dot) == 2
  assert -500 <= dot[0] <= 500 and dot[0] != 0
  assert -500 <= dot[1] <= 500 and dot[1] != 0

  return (dot[0]*dot[1] < 0) + (dot[1] < 0)*2 + 1