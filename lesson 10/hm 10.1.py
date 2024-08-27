from inspect import isgenerator


def mu_funk(x):
    return x ** 2


def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """

    while end > 0:
        yield begin
        begin = func(begin)
        end -= 1


gen = some_gen(2, 4, mu_funk)
assert isgenerator(gen) is True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
