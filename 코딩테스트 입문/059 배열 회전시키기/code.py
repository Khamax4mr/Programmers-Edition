def solution(numbers, direction):
  assert 3 <= len(numbers) <= 20
  assert direction in {"left", "right"}

  if direction == "left":
    return numbers[1:] + numbers[:1]
  else:
    return numbers[-1:] + numbers[:-1]