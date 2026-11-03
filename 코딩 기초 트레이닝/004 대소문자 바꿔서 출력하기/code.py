def solution(str):
  # 코딩 테스트 전용 입력문.
  # str= input()

  assert 1 <= len(str) <= 20
  assert str.isalpha()
  
  print(str.swapcase())

  # 테스트 드라이버 실행용 리턴문.
  return str.swapcase()