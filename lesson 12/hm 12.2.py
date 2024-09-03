class Product:

    def __init__(self, name, price,  description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'{self.name}, вартість: {self.price}'


class User:

    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

    def __str__(self):
        return f'{self.name} {self.surname}'


class Order:

    def __init__(self, user):
        self.user = user
        self.product = {}
        self.total = 0

    def add_product(self,  item, cnt):
        self.product[item] = cnt

    def get_total(self):
        self.total = 0
        for cost, num in self.product.items():
            self.total += cost.price * num
        return self.total

    def __str__(self):
        result = f'Користувач: {self.user}\nСписок покупок:'
        for item, cnt in self.product.items():
            result += f'\n{item.name}: {cnt} шт.'
        return result


pants = Product('Штани', 700, 'синій', 'XL')
shirt = Product('Сорочка', 430, 'червоний', 'M')
shorts = Product('Шорти', 380, 'блакитний', 'M')
jacket = Product('Куртка', 799, 'зелений', 'S')

person_one = User('Мирослава', 'Вареник', '0967853421')

cart = Order(person_one)
cart.add_product(shirt, 1)
cart.add_product(pants, 2)

print(cart)
print(f'Ціна: {cart.get_total()} грн')


assert isinstance(cart.user, User) is True
assert cart.get_total() == 1830
assert cart.get_total() == 1830
cart.add_product(pants, 10)
print(cart)
print(f'Ціна: {cart.get_total()} грн')
