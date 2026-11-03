def solution(inp):
  # 코딩 테스트 전용 입력문.
  # a, b = map(int, input().strip().split(' '))

  a, b = map(int, inp.strip().split(' '))
  assert 1 <= a <= 100
  assert 1 <= b <= 100

  print(f"{a} + {b} = {a + b}")
  
  # 테스트 드라이버 실행용 리턴문.
  return f"{a} + {b} = {a + b}"