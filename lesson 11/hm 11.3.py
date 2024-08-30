def is_even(number: int) -> bool:
    my_list = [0, 1, 3, 5, 7, 9]
    if number in my_list or int(str(number)[-1]) in my_list:
        return False
    else:
        return True


assert is_even(2494563894038**2) is True, 'Test1'
assert is_even(1056897**2) is False, 'Test2'
assert is_even(24945638940387**3) is False, 'Test3'
print('ok')
