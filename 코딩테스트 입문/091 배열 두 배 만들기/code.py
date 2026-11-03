def solution(numbers):
  assert 1 <= len(numbers) <= 1000
  assert all(-10000 <= n <= 10000 for n in numbers)

  return [n*2 for n in numbers]