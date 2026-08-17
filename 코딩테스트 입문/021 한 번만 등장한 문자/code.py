def solution(s):
  assert s.islower()
  assert 0 < len(s) < 1000

  return "".join(sorted(i for i in set(s) if s.count(i) == 1))