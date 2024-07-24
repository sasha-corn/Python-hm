number = int(input("Введіть 4-х значне число: "))

number01 = number // 1000
number = number - number01 * 1000
number02 = number // 100
number = number - number02 * 100
number03 = number // 10
number = number - number03 * 10
number04 = number // 1

print(number01)
print(number02)
print(number03)
print(number04)
