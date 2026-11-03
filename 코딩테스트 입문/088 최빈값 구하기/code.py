from collections import Counter

def solution(array):
  assert 0 < len(array) < 100
  assert all(0 <= n < 1000 for n in array)
  
  cnts = Counter(array).most_common(2)
  return cnts[0][0] if len(cnts) == 1 or cnts[0][1] > cnts[1][1] else -1