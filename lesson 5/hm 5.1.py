import string
import keyword

name = input("Введіть ім'я змінної: ")

if name in keyword.kwlist or name[0].isdigit():
    print(False)
elif name != "_" and name.islower() is False:
    print(False)
else:
    for char in name:
        if char != '_' and char in string.punctuation or char == ' ':
            print(False)
            break
    print(True)
