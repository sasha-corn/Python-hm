numbers = [21, 56, 4, 25, 777, 102, 3]

if len(numbers) == 0:
    print(numbers)
else:
    numbers.insert(0, numbers.pop(-1))
    print(numbers)
