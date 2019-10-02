from IMClasses import Category, Catalog, Product, Order, BaseDiscount, SaleDiscount, CategoryDiscount

category3 = Category(name='notebooks', label='Ноутбуки')
product4 = Product(category=category3, name='Ноутбук Dell', price=300)
product5 = Product(category=category3, name='Ноутбук Asus', price=200)

if product4 > product5:
    print(f'"{product4}" дороже чем "{product5}"')
elif product4 == product5:
    print(f'"{product4}" и "{product5}" - продаются по одной цене')
else:
    print(f'"{product4}" дешевле чем "{product5}"')


order1 = Order(products=[product4, product5])
order2 = Order(products=[product4])

if order1 > order2:
    print(f'"{order1}" дороже чем "{order2}"')
elif order1 == order2:
    print(f'"{order1}" и "{order2}" - равны по цене')
else:
    print(f'"{order1}" дешевле чем "{order2}"')


base_discount = BaseDiscount()
sale_discount = SaleDiscount(size=70)

if base_discount > sale_discount:
    print(f'"{base_discount}" наиболее выгодная')
elif base_discount == sale_discount:
    print(f'Скидки равнозначны - берите любую')
else:
    print(f'"{sale_discount}" наиболее выгодная')
