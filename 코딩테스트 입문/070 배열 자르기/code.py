def solution(numbers, num1, num2):
  assert 2 <= len(numbers) <= 30
  assert 0 <= num1 < num2 < len(numbers)
  assert all(0 <= n <= 1000 for n in numbers)

  return numbers[num1:num2+1]