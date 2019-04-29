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
