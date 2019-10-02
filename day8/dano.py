from IMClasses import Category, Catalog, Product, Order, BaseDiscount, SaleDiscount, CategoryDiscount

category1 = Category(name='fridges', label='Холодильники')
category2 = Category(name='tvs', label='Телевизоры')
category3 = Category(name='notebooks', label='Ноутбуки')
print(category1)  # выводить "Холодильники (label=fridges)" - Подсказка! см. __str__

product1 = Product(category=category1, name='Холодильник LG', price=300)
product2 = Product(category=category2, name='Телевизор Samsung', price=200)
product3 = Product(category=category3, name='Ноутбук MacBookPro', price=400)
product4 = Product(category=category3, name='Ноутбук Dell', price=300)
product5 = Product(category=category3, name='Ноутбук Asus', price=200)
print(product1)  # выводить "Холодильник LG (price=300, category=Холодильники (label=fridges))"

catalog = Catalog([category1, category2, category3])
catalog.show(limit=1)
"""выводит
- Холодильники
- Телевизоры
- Ноутбуки
"""

order = Order(products=[product1, product2])

# Есть возможность добавить товар в заказ
order.add(product3)
order.add(product3)
order.add(product3)
order.add(product4)
order.add(product5)


order.show()
"""выводит
- Холодильники
    - Холодильник LG - штук=1 - цена=300 
- Телевизоры
    - Телевизор Samsung - штук=1 - цена=200
- Ноутбуки
    - Ноутбук MacBookPro - штук=3 - цена=1200
    - Ноутбук Dell - штук=1 - цена=300
    - Ноутбук Asus - штук=1 - цена=200
"""
# Есть возможность удалить товар из заказа
order.remove(product3)

# Возвращает сумму заказа - общую
order.total_price()
# Выводит "Общая сумма заказа: 1800"

print(order)
# Выводит "Заказ №a84d3371-6435-4933-8900-ef48b67ce049 на сумму 1800"
# Здесь "a84d3371-6435-4933-8900-ef48b67ce049" -
# это universally unique identifier "универсальный уникальный идентификатор"
# https://docs.python.org/3.7/library/uuid.html Подсказка - "uuid4"

# Так же в нашем магазине должен быть функционал скидок.
# Класс должен уметь внутри себя взять и подсчитать цену за весь заказ, с учётом скидки.
discount = BaseDiscount() # базовая скидка 10%
print(discount)  # выводит "Базовая Скидка - 10%"

sale_discount = SaleDiscount(size=70)
print(sale_discount)  # выводит "Скидка по распродаже - 70%"

category_discount = CategoryDiscount(size=30, category=category3)
print(category_discount)  # выводит "Скидка на 'Ноутбуки' - 30%"

order.apply_discount(category_discount) # применили скидку на категорию "Ноутбуки"
order.show()
"""выводит
- Холодильники
    - Холодильник LG - штук=1 - цена=300 
- Телевизоры
    - Телевизор Samsung - штук=1 - цена=200
- Ноутбуки
    - Ноутбук MacBookPro - штук=2 - цена=800 - скидка=240 - новаяцена=560
    - Ноутбук Dell - штук=1 - цена=300 - скидка=90 - новаяцена=210
    - Ноутбук Asus - штук=1 - цена=200 - скидка=60 - новаяцена=140
"""
order.total_price()
# Выводит "Общая сумма заказа: 1410, с учётом скидок"