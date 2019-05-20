# task3:
# Написать программу которая принимает от пользователя 2 целых числа!. Передает их в функцию которая делит их и
# возвращает результат деления. Выводит результат деления на экран если не было исключения.
# Внутри функции надо подключить модуль import hahaha если первое число больше второго, и модуль import sys
# если второе больше первого.
# Вызов этой функции, есть опасная затея, поэтому обернем вызов в try .. except.
# Если результат без остатка, возвращаем его для дальнейшего вывода.
# Если результат с остатком, инициируем исключение типа «Арифметическая Ошибка» в сообщении
# которому передаем результат деления, Ссылка https://docs.python.org/3/library/exceptions.html в помощь
# Если исключения не было, выводим сообщение «поделили успешно, вот вам результат:»
# Не забываем про другие возможные в данном контексте исключения, тут просто выводим на экран «Не предвиденная ошибка».
# Все исключения отлавливаем в отдельном блоке except.


def isint(num):

    try:
        int(num)
    except ValueError:
        return False
    else:
        return True


def nevedomaya_func(divident, divisor):

    try:
        result = divident/divisor
    except ZeroDivisionError as e:
        print('Ошибка деления на ноль', e)
    else:
        if divident > divisor:
            import hahaha
        elif divisor > divident:
            import sys
        if result.is_integer():
            return result
        else:
            raise(ArithmeticError('Ошибка, результат деления: {}'.format(result)))


while True:

    try:
        num1, num2 = input('Введите два целых числа:  ').split()
    except ValueError:
        print('Непредвиденная ошибка')
    else:

        if isint(num1) and isint(num2):

            try:
                result = nevedomaya_func(int(num1), int(num2))
            except ImportError:
                print('Непредвиденная ошибка')
            except ArithmeticError as e:
                print(e)
                break
            else:
                print('Поделили успешно, вот вам результат: ', int(result), sep='')
                break

        else:
            print('Числа должны быть целыми!')
            continue
