import heapq

def solution(numbers):
  assert 2 <= len(numbers) <= 100
  assert all(0 <= n <= 10000 for n in numbers)

  largest = heapq.nlargest(2, numbers)
  return largest[0] * largest[1]