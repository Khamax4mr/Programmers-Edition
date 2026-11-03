def solution(inp):
  # 코딩 테스트 전용 입력문.
  # str, n = input().strip().split(' ')

  str, n = inp.strip().split(' ')
  n = int(n)
  assert 1 <= len(str) <= 10
  assert 1 <= n <= 5
  
  print(str * n)

  # 테스트 드라이버 실행용 리턴문.
  return str * n