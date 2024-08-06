
result = 0
answer = input('Хочете почати роботу з калькулятором?(y/n) => ')

while answer == 'y':
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
        while number2 == 0:
            print("ділити на 0 не можна, ведіть інше число")
            number2 = int(input('введіть 2 число: '))
        result = number1 / number2

    print(number1, act, number2, ' = ', result)
    answer = input('Чи хочете продовжити?(y/n) => ')
