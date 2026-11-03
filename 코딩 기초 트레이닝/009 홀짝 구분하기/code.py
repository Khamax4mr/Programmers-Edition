def solution(n):
  # 코딩 테스트 전용 입력문.
  # n = int(input())

  assert 1 <= n <= 1000

  result = ["even", "odd"]
  print(f"{n} is {result[n%2]}")
  
  # 테스트 드라이버 실행용 리턴문.
  return f"{n} is {result[n%2]}"