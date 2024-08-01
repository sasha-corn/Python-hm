lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

print('Список до сортування: ', lst)

for _ in lst:
    if _ == 0:
        lst.append(lst.pop(lst.index(_)))

print('Список після сортування: ', lst)
