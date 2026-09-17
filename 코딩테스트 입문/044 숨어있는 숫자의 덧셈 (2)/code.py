from re import sub

def solution(my_string):
  assert 1 <= len(my_string) <= 1000

  nums = list(map(int, sub(r"[a-zA-Z]", " ", my_string).strip().split()))
  assert all(1 <= n <= 1000 for n in nums)
  return sum(nums)