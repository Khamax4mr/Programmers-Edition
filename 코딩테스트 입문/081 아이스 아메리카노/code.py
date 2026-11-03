def solution(money):
  assert 0 < money <= 10000000

  return list(divmod(money, 5500))