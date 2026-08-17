def solution(my_string):
  assert 5 <= len(my_string) <= 100
  
  tokens = my_string.split()
  assert len(tokens) & 1

  nums, opers = tokens[::2], tokens[1::2]
  assert len(opers) >= 1
  assert all(1 <= int(n) <= 20000 for n in nums)
  assert all(op in {"+", "-"} for op in opers)
  
  temp = int(nums[0])
  for i in range(len(opers)):
    temp += int(opers[i] + nums[i+1])
    assert -100000 <= temp <= 100000
    
  return temp