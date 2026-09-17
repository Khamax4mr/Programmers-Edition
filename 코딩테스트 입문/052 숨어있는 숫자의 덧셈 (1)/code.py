from re import sub

def solution(my_string):
  assert my_string.isalnum()
  assert 1 <= len(my_string) <= 1000

  nums = list(map(int, list(sub(r"[a-zA-Z]", "", my_string).strip())))
  assert all(0 <= n <= 9 for n in nums)
  return sum(nums)