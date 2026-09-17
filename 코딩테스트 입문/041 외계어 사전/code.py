from re import compile

def solution(spell, dic):
  assert 2 <= len(spell) == len(set(spell)) <= 10
  assert 1 <= len(dic) == len(set(dic)) <= 10
  assert all(len(c) == 1 and c.islower() for c in spell)
  assert all(1 <= len(word) <= 11 and word.islower() for word in dic)

  pattern = compile("^[" + "".join(spell) + "]{" + str(len(spell)) + "}$")
  return 2 - any(len(word) == len(set(word)) and pattern.match(word) is not None for word in dic)