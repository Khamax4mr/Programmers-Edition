from math import gcd

def solution(numer1, denom1, numer2, denom2):
  assert 0 < numer1 < 1000
  assert 0 < denom1 < 1000
  assert 0 < numer2 < 1000
  assert 0 < denom2 < 1000

  numer3 = numer1*denom2 + numer2*denom1
  denom3 = denom1*denom2
  cd = gcd(denom3, numer3)

  return [numer3//cd, denom3//cd]