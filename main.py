from csv import DictWriter, DictReader
from os.path import exists


def create_file():
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()


def get_info():
    while True:
        info = input('Введите данные через запятую в виде {Иванов, Иван, 8 961 862 46 47}: ').split(', ')
        if len(info) == 3 or info == 'q':
            break
        else:
            print('Ошибка!\nПример: Иванов, Иван, 8 961 862 46 47')
    return info


def get_update_info():
    while True:
        info = input('Введите данные для обновления в виде {Иванов, Иван}: ').split(', ')
        if len(info) == 2 or info == 'q':
            break
        else:
            print('Ошибка!\nПример: Иванов, Иван')
    return info


def write_file(lst):
    res = list()
    with open('phone.csv', 'r', encoding='utf-8', newline='') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        for el in res:
            if el['Номер'] == obj['Номер']:
                print('Человек с таким номером телефона уже существует.\nДанные не добавленны')
                return
        res.append(obj)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)


def update_file(new_info, pk):
    '''
    :param new_info: информация которая будет записана
    :param pk: ищем человека по номеру телефона
    :return: записаные измененния в файле
    '''
    with open('phone.csv', 'r+', encoding='utf-8', newline='') as data:
        f_reader = DictReader(data)
        res = []
        for el in f_reader:
            obj = {'Фамилия': new_info[0], 'Имя': new_info[1]}
            if el['Номер'] == pk:
                el['Фамилия'] = obj['Фамилия']
                el['Имя'] = obj['Имя']
            print(el)
            res.append(el)
        with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
            f_writer.writeheader()
            f_writer.writerows(res)


def delete_file(pk):
    with open('phone.csv', 'r+', encoding='utf-8', newline='') as data:
        f_reader = DictReader(data)
        res = []
        for el in f_reader:
            if el['Номер'] != pk:
                res.append(el)

        with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
            f_writer.writeheader()
            f_writer.writerows(res)
        print('Данные удалены')


def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    return res


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                create_file()
            print(read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
            write_file(get_info())
        elif command == 'u':
            if not exists('phone.csv'):
                create_file()
            pk = input('Введите номер человека, данные которого изменить: ')
            if pk.isdigit():
                update_file(get_update_info(), pk)
            else:
                print('Ошибка: pk должен быть целым числом')
        elif command == 'd':
            if not exists('phone.csv'):
                create_file()
            pk = input('Введите номер человека, данные которого удалить: ')
            if pk.isdigit():
                delete_file(pk)
            else:
                print('Ошибка: pk должен быть целым числом')


main()
