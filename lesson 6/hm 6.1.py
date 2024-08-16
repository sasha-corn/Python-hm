import string

letter = tuple(input('Введіть літери через дефіз: '))
abc = string.ascii_letters
letters = abc[abc.index(letter[0]):(abc.index(letter[2]) + 1)]
print(letters)
