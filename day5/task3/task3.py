# task 3
# Возьми пример со слайда 3 https://slides.com/corianderza/closures_decorators/live#/0/2
# и реализуй его плохим способом, т.е БЕЗ исподльзования декоратора


def decor(some_params):
    def wrapper(func):
        print(some_params)
        return func
    return wrapper


def pr_func():
    print('hi')


pr_func = decor('some_params')(pr_func)
print('---')
pr_func()

# Рузультат:
# $ python3 task3.py
# some_params
# hi

