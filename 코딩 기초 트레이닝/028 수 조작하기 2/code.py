def solution(numLog):
  assert 2 <= len(numLog) <= 100000
  assert -100000 <= numLog[0] <= 100000

  diff = [numLog[i+1] - numLog[i] for i in range(len(numLog)-1)]
  assert all(n in [-10, -1, 1, 10] for n in diff)

  movement = {1: "w", -1: "s", 10: "d", -10: "a"}
  return "".join(movement[n] for n in diff)