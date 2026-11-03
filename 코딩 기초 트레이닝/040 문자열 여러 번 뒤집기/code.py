def solution(my_string, queries):
  assert my_string.islower()
  assert 1 <= len(my_string) <= 1000
  assert 1 <= len(queries) <= 1000
  assert all(0 <= s <= e <= len(my_string) for s, e in queries)

  for s, e in queries:
    my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

  return my_string