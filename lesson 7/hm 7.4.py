
def common_elements():
    set_for3 = set()
    set_for5 = set()
    set_for3.update(char for char in range(101) if char % 3 == 0)
    set_for5.update(char for char in range(101) if char % 5 == 0)
    return set_for3.intersection(set_for5)


print(common_elements())
