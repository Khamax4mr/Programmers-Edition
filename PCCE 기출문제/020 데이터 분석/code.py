from datetime import datetime

def solution(data, ext, val_ext, sort_by):
  key = ["code", "date", "maximum", "remain"]
  assert ext in key
  assert sort_by in key
  assert (ext != "code") or (1 <= val_ext <= 100000)
  assert (ext != "date") or (20000101 <= val_ext <= 29991231)
  assert (ext != "maximum") or (1 <= val_ext <= 10000)
  assert (ext != "remain") or (1 <= val_ext <= 10000)
  assert 1 <= len(data) <= 500

  for code, date, maximum, remain in data:
    assert 1 <= code <= 100000
    assert 20000101 <= date <= 29991231
    assert 1 <= remain <= maximum <= 10000
    try:
      year, temp = divmod(date, 10000)
      month, day = divmod(temp, 100)
      datetime(year, month, day)
    except ValueError:
      assert False

  id = {item: i for i, item in enumerate(key)}
  assert len(data) == len(set(line[id[ext]] for line in data))
  
  return sorted([line for line in data if line[id[ext]] < val_ext], key=lambda x: x[id[sort_by]])