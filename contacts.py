
from os.path import exists

def add_op(data, colums):
    print("Необходимо заподнить данные: ")
    flag = True
    while flag:
        colums = colums_op(data)
        user = {}
        for colum in colums:
            user[colum] = input(colum + " : ")
        save = input("\n Нажмите 1 для сохранения либо любую другую цифру для выхода")
        if save == "1":
            write_op(user, data)
        flag = False



def write_op(user, data):
    data.append(user) 



def write_data(data, colums):
    with open (file, 'w', encoding = 'utf-8') as f:
        f.write(", ".join(colums) + "\n")
        for user in data:
            f.write(", ".join(user.values()) + "\n")


# def read_op():
#     with open (file, 'r', encoding = 'utf-8') as f:
#         data = f.read()
#         print(data)
        
def read_data_op():
    valid = exists(file)
    if not valid:
        return []
    with open (file, 'r', encoding = 'utf-8') as f:
        data = f.read()
        if len(data.split()) < 2:
            return []
        colums = data[0].strip().split("; ")
        data = [{colums[i]: user.strip().split("; ")[i] for i in range(len(colums))} for user in data.split()[1:]]
        return data

def colums_op(data):
    if not data:
        return ["Фамилия", "Имя"]
    colums = data[0].keys()
    return colums



def add_colums_op(data, column, colums):
    for user in data:
        user[column] = ""
    colums.append(column)
    return data


def input_colums():
    return input("Введите имя нового столбца: ")


def find_op(data):
    column = input("Введите столбец: ")
    val = input("Введите значение: ")
    flag = False
    for user in data:
        if column not in user:
            return "Такого столбца нет"
        if user[column] == val:
            print(user)
    if not flag:
        print("Данных нет")

file = 'data_base.csv'

# valid = exists(file)
# if not valid:
#     new_file()


