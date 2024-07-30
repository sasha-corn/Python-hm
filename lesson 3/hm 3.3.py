first_list = [1, 2, 3, 4, 5, 6]

half = (len(first_list) + 1) // 2
print(half)
one_min = first_list[:half]
two_min = first_list[half:]
secnd_list = [one_min, two_min]
print(secnd_list)
