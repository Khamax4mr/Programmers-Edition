def solution(inp):
  # 코딩 테스트 전용 입력문.
  # a, b = map(int, input().strip().split(' '))

  a, b = map(int, inp.strip().split(' '))
  assert -100000 <= a <= 100000
  assert -100000 <= b <= 100000
  
  print(f"a = {a}")
  print(f"b = {b}")

  # 테스트 드라이버 실행용 리턴문.
  return "\n".join([f"a = {a}", f"b = {b}"])