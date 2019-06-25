from uuid import uuid4


class Category:
    def __init__(self, name, label):
        self.name = name
        self.label = label

    def __str__(self):
        return '{0} (label={1})'.format(self.label,
                                        self.name)


class Catalog:
    def __init__(self, category_list):
        self.catalog = category_list

    def show(self, limit):
        for i in range(limit):
            print(self.catalog[i].label)


class Product:
    def __init__(self, category, name, price):
        if isinstance(category, Category):
            self.category = category
        self.name = name
        self.price = price

    def __str__(self):
        return '{0} (price={1}, category={2} (label={3}))'.format(self.name,
                                                                  self.price,
                                                                  self.category.label,
                                                                  self.category.name)

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __eq__(self, other):
        return self.price == other.price


class Order:
    def __init__(self, products: list):
        self.products = products
        self.uuid = uuid4()
        self.discount = None
        self._discounted_products = {}
        self.total = self._calculate_total_price()

    def _calculate_total_price(self):
        total = 0
        if self.discount:
            if self.discount.category:
                for product in self.products:
                    if product.category == self.discount.category:
                        self._discounted_products[product] = int(product.price - product.price * self.discount.coefficient)
                        total += product.price * self.discount.coefficient
                    else:
                        total += product.price
            else:
                for product in self.products:
                    self._discounted_products[product] = int(product.price - product.price * self.discount.coefficient)
                    total += product.price * self.discount.coefficient
        else:
            total = sum([product.price for product in self.products])

        return int(total)

    def add(self, product):
        self.products.append(product)
        self.total = self._calculate_total_price()

    def show(self):
        category_set = {product.category for product in self.products}
        for category in category_set:
            print('- {}'.format(category.label))
            for product in set(self.products):
                amount = self.products.count(product)
                if product.category == category:
                    if product in self._discounted_products.keys():
                        print('    - {0} - штук={1} - цена={2} - скидка={3}'
                              ' - новая цена={4}'.format(product.name,
                                                         amount,
                                                         product.price * amount,
                                                         self._discounted_products[product] * amount,
                                                         (product.price - self._discounted_products[product]) * amount))
                    else:
                        print('    - {0} - штук={1} - цена={2}'.format(product.name,
                                                                       self.products.count(product),
                                                                       product.price,
                                                                       ))

    def apply_discount(self, discount):
        self.discount = discount
        self.total = self._calculate_total_price()

    def remove(self, product):
        if product in self.products:
            self.products.remove(product)
            self.total = self._calculate_total_price()

    def total_price(self):
        if self.discount:
            print('Общая сумма заказа: {0}, с учетом скидок'.format(self.total))
        else:
            print('Общая сумма заказа: {0}'.format(self.total))

    def __str__(self):
        return 'Заказ №{0} на сумму {1}'.format(self.uuid,
                                                self.total)

    def __lt__(self, other):
        return self.total < other.total

    def __gt__(self, other):
        return self.total > other.total

    def __eq__(self, other):
        return self.total == other.total


class BaseDiscount:
    def __init__(self, size=10):
        self.size = size
        self.coefficient = 1 - self.size / 100
        self.category = None

    def __str__(self):
        return 'Базовая Скидка - 10%'

    def __lt__(self, other):
        return self.size < other.size

    def __gt__(self, other):
        return self.size > other.size

    def __eq__(self, other):
        return self.size == other.size


class SaleDiscount(BaseDiscount):
    def __init__(self, size):
        super().__init__(size)

    def __str__(self):
        return 'Скидка по распродаже - {}%'.format(self.size)


class CategoryDiscount(SaleDiscount):
    def __init__(self, size, category):
        super().__init__(size)
        self.category = category

    def __str__(self):
        return 'Скидка на \'{0}\' - {1}%'.format(self.category.label, self.size)
