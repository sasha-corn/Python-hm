first_list = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6, 7]
c = []

half = (len(first_list) + 1) // 2
one_min = first_list[:half]
two_min = first_list[half:]
thrt_list = [one_min, two_min]
print(thrt_list)

half = (len(b) + 1) // 2
print(half)
one_min = b[:half]
two_min = b[half:]
thrt_list = [one_min, two_min]
print(thrt_list)

half = (len(c) + 1) // 2
print(half)
one_min = c[:half]
two_min = c[half:]
thrt_list = [one_min, two_min]
print(thrt_list)
