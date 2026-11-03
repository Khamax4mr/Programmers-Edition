def solution(numbers):
  assert 1 <= len(numbers) <= 100
  assert all (0 <= n <= 1000 for n in numbers)

  answer = sum(numbers) / len(numbers)
  assert not ((answer * 2) % 1)
  return answer