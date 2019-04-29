# task 1:
# Оберните функцию в хлеб, кетчуп и сыр, используя один декоратор.


def sandwich(func):
    def wrapper(meat):
        print('----хлеб----')
        print('---кутчуп---')
        print('----сыр-----')
        func(meat)
        print('----хлеб----')
    return wrapper


@sandwich
def mainingredient(meat):
    print('---%s---' % meat)


mainingredient('ветчина')

# Результат:
# $ python3 task1.py
# ----хлеб----
# ---кутчуп---
# ----сыр-----
# ---ветчина---
# ----хлеб----
