from itertools import product

def solution(l, r):
  assert 1 <= l <= r <= 1000000

  cands = []
  for cand in product((0, 5), repeat=len(str(r))+1):
    n = int("".join(map(str, cand)))
    if not l <= n <= r: continue
    cands.append(n)
    
  return cands if cands else [-1]