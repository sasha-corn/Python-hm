import string

my_line = input('Ведіть речення: ')
my_line = ''.join(char for char in my_line if char not in string.punctuation)
my_line = '#' + my_line.title().replace(' ', '')

print(my_line[:141])
