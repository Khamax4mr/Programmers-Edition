from re import fullmatch

def solution(s):
  assert fullmatch(r"-?(0|[1-9][0-9]*)(\s(Z|-?(0|[1-9][0-9]*)))*", s)
  assert 1 <= len(s) <= 200

  total = 0
  for i in range(len(s := s.split())):
    n = int(s[i]) if s[i] != "Z" else -int(s[i-1]) 
    assert -1000 < n < 1000
    total += n
  return total