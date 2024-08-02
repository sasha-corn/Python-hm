import random

frst_list = [random.randint(0, 10) for _ in range(random.randint(3, 10))]
print(frst_list)

scnd_list = [frst_list[0], frst_list[2], frst_list[-2]]
print(scnd_list)
