# task 4:
# Напиши «плохой» пример — выполнение декоратора без использования синтаксиса декоратора.
# Т.е сделай это просто вызывая функции и передавая им параметром другие функции.
# Сделай функцию def regural_car () которая производит обычнею машину. Ну, например так:
# print("Lada седан, баклажан").
# Затем сделай из обычной машины спортивную (добавь к обычной машине спойлер, спортивные колеса).


def car_factory(*args):
    def make_it_sport(func):
        def wrapped(car, color):
            print('Было: ')
            func(car, color)
            print('Стало: \n{} - спорткар. Комплектация: {}'.format(car, ', '.join(args)))
            return func
        return wrapped
    return make_it_sport


# @car_factory('спойлер', 'спортивные колеса')
def regular_car(car, color):
    print('{} седан, {}'.format(car, color))


regular_car = car_factory('спойлер', 'спортивные колеса')(regular_car)
regular_car('Lada', 'баклажан')

# Результат:
# $ python3 task4.py
# Было:
# Lada седан, баклажан
# Стало:
# Lada - спорткар. Комплектация: спойлер, спортивные колеса
