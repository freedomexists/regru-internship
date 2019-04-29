# task 2:
# Из первой задачи разделите один декоратор на два: отдельно хлеб,
# отдельно ингредиенты. Опробуйте использование нескольких декораторов


def bread(func):
    def wrapper(meat):
        print('----хлеб----')
        func(meat)
        print('----хлеб----')
    return wrapper


def ingredients(func):
    def wrapper(meat):
        print('---кетчуп---')
        print('----сыр-----')
        func(meat)
    return wrapper


@bread
@ingredients
def mainingredient(meat):
    print('---{}---'.format(meat))


mainingredient('ветчина')

# Результат:
# $ python3 task2.py
# ----хлеб----
# ---кетчуп---
# ----сыр-----
# ---ветчина---
# ----хлеб----