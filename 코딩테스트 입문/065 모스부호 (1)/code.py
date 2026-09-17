def solution(letter):
  assert "  " not in letter and not letter.startswith(" ") and not letter.endswith(" ")
  assert 1 <= len(letter) <= 1000

  morse = {
    '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
    '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n',
    '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u',
    '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z'
  }
  return "".join([morse[token] for token in letter.split()])