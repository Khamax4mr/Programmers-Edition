def solution(emergency):
  assert 1 <= len(emergency) == len(set(emergency)) <= 10
  assert all(1 <= e <= 100 for e in emergency)

  rank = {e: i+1 for i, e in enumerate(sorted(emergency, reverse=True))}
  return [rank[e] for e in emergency]