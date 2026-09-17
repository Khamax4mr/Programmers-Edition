def solution(rsp):
  assert set(rsp) <= {"0", "2", "5"}
  assert 0 < len(rsp) <= 100

  prs = {"2": "0", "0": "5", "5": "2"}
  return "".join(prs[i] for i in list(rsp))