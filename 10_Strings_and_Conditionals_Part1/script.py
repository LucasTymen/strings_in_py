
def letter_check(word, letter):
  for character in word:
    if character == letter:
     return True
  return False

letter_check("barbarians","a")
print(letter_check("barbarians","a"))
