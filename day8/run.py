from solution import FileReader


if __name__ == '__main__':
    pth = input('Введите путь до файла: \n')
    file = FileReader(pth)
    print(file.read())
