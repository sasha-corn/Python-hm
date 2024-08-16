def second_index(text, some_str):
    index = text.find(some_str, text.index(some_str) + 1) if some_str in text else None
    return index


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "H") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
