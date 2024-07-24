number = int(input("Введіть 5-ти значне число: "))

number01 = number // 10000
number = number - number01 * 10000
number02 = number // 1000
number = number - number02 * 1000
number03 = number // 100
number = number - number03 * 100
number04 = number // 10
number = number - number04 * 10
number05 = number // 1

number = (number05 * 10000) + (number04 * 1000) + (number03 * 100) + (number02 * 10) + number01
print(number)
