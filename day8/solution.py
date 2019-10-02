# task1:
# Для разогрева. Ваша задача написать Python-модуль solution.py, внутри которого определен класс FileReader.
# Инициализатор этого класса принимает аргумент — путь до файла на диске.
# У класса должен быть метод read, возвращающий содержимое файла в виде строки.
# Не забываем обрабатывать ошибки работы с файлом.
# Ну и должен быть какой-то скрипт например run.py, который будет использовать ваш класс.


class FileReader:
    def __init__(self, pth_to_file):
        self.pth_to_file = pth_to_file

    def read(self):
        try:
            f = open(self.pth_to_file, 'r')
        except PermissionError:
            print('Ошибка доступа к файлу ', self.pth_to_file)
        except FileNotFoundError:
            print('Файл не существует')
        else:
            return f.read()
