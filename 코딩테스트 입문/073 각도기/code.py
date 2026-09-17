def solution(angle):
  assert 0 < angle <= 180
  
  return (angle > 0) + (angle >= 90) + (angle > 90) + (angle >= 180)