number1 = int(input('введіть 1 число: '))
number2 = int(input('введіть 2 число: '))
act = input('введіть дію: ')


if act == '+':
    result = number1 + number2
elif act == '-':
    result = number1 - number2
elif act == '*':
    result = number1 * number2
elif act == '/':
    if number2 == 0:
        print("ділити на 0 не можна, ведіть інше число")
        number2 = int(input('введіть 2 число: '))
    result = number1 / number2

print(number1, act, number2, ' = ', result)
