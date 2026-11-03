def solution(price):
  assert 10 <= price <= 1000000
  assert not (price % 10)

  discount_val = [100000, 300000, 500000, 500000]
  return int(price * (1 - 0.05*sum(price >= d for d in discount_val)))