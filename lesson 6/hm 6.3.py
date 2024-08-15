numbers = tuple(input('Введіть число: '))

suma = 10
while suma > 9:
    suma = 1
    numbers = list(numbers)
    for part in numbers:
        suma *= int(part)
    numbers.clear()
    numbers = tuple(str(suma))


print('Результат: ', suma)
