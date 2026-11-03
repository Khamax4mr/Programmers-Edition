def solution(inp):
  # 코딩 테스트 전용 입력문.
  # str1, str2 = input().strip().split(' ')

  str1, str2 = inp.strip().split(' ')
  assert 1 <= len(str1) <= 10
  assert 1 <= len(str2) <= 10

  print(str1 + str2)
  
  # 테스트 드라이버 실행용 리턴문.
  return str1 + str2