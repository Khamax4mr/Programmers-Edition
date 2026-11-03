def solution(my_strings, parts):
  assert 1 <= len(my_strings) == len(parts) <= 100
  assert all(1 <= len(s) <= 100 for s in my_strings)
  assert all(0 <= p[0] <= p[1] < len(s) for s, p in zip(my_strings, parts))

  return "".join(s[p[0]:p[1]+1] for s, p in zip(my_strings, parts))