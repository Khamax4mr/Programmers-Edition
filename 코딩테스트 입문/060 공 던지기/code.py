def solution(numbers, k):
  assert 0 < k < 1000
  assert numbers == sorted(numbers)
  assert 2 <= len(numbers) <= 100

  loop = numbers[::2] + (numbers[1::2] if len(numbers) % 2 else [])
  return loop[k % len(loop) - 1]