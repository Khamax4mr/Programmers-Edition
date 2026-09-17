def solution(n):
  # 풀이용 입력문.
  # n = int(input())
  assert 1 <= n <= 10

  print("\n".join("*"*(i+1) for i in range(n)))

  # 테스트 드라이버 실행용 리턴문.
  return "\n".join("*"*(i+1) for i in range(n))