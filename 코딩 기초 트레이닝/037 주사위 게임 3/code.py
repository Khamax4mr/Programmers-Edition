from collections import Counter

def solution(a, b, c, d):
  assert 1 <= a <= 6 and str(a).isdigit()
  assert 1 <= b <= 6 and str(b).isdigit()
  assert 1 <= c <= 6 and str(c).isdigit()
  assert 1 <= d <= 6 and str(d).isdigit()

  cnts = Counter([a, b, c, d])
  max_n = max(cnts, key=cnts.get)

  match cnts[max_n]:
    case 1:
      return min(cnts)
    case 2:
      if len(cnts) == 2:
        p, q = cnts.keys()
        return (p + q) * abs(p - q)
      else:
        _, q, r = sorted(cnts, key=cnts.get, reverse=True)
        return q * r
    case 3:
      p, q = sorted(cnts, key=cnts.get, reverse=True)
      return (10*p + q) ** 2
    case 4:
      return 1111*a