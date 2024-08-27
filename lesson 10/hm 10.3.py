def is_even(digit):
    """ Перевірка чи є парним число """
    result = False
    if digit % 2 == 0:
        result = True
    return result


assert is_even(2) is True, 'Test1'
assert is_even(5) is False, 'Test2'
assert is_even(0) is True, 'Test3'
print('OK')
