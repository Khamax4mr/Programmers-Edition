def solution(my_string, letter):
  assert my_string.isalpha() and letter.isalpha()
  assert 1 <= len(my_string) <= 100
  assert len(letter) == 1

  return my_string.replace(letter, "")