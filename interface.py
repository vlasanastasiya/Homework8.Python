
from contacts import colums_op, input_colums, read_data_op, add_op, add_colums_op, input_colums, write_data, find_op


def interface_menu():
    data = read_data_op()
    colums = colums_op(data)
    flag = True
    while flag:
        print('\nЗдравствуйте! Это база данных! Выберите соответствующую цифру в меню: ')
        while True:
            print('1 - Найти контакт')
            print('2 - Добавить контакт')
            print('3 - Показать все контакты')
            print('4 - Добавить столбец')
            print('5 - выход')
            choice = input()
            if choice not in ["1", "2", "3", "4", "5"]:
                print('Выберите другую цифру меню. ')
                continue
            elif choice == "1":
                find_op(data)
                break
            elif choice == "2":
                add_op(data, colums)
                break
            elif choice == "3":
                print(colums)
                print(data)
            elif choice == "4":
                column = input_colums()
                data = add_colums_op(data, column, colums)
            else:
                flag = False
                write_data(data, colums)
                break