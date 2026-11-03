def solution(number):
  assert 1 <= len(number) <= 100000
  assert number.isdigit()
  assert not number.startswith("0") or number == "0"

  return sum(map(int, number)) % 9