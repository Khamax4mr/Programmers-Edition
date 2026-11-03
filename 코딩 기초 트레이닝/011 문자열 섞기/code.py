def solution(str1, str2):
  assert str1.islower()
  assert str2.islower()
  assert 1 <= len(str1) == len(str2) <= 10

  return "".join(s1 + s2 for s1, s2 in zip(str1, str2))