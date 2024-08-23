def difference(*args):
    if len(args) > 0:
        max_numb = max(args)
        min_numb = min(args)
        result = max_numb - min_numb
    else:
        result = 0

    return round(result, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
