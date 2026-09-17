def solution(age):
  assert 0 < age <= 1000

  return "".join(chr(int(i)+97) for i in str(age))