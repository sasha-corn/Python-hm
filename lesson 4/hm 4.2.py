lst = [1, 3, 5]
lst_two = lst[::2]

sum_step = 0
if len(lst) == 0:
    print(0)
else:
    for _ in lst_two:
        sum_step += _
    else:
        sum_step *= lst[-1]
        print(sum_step)
