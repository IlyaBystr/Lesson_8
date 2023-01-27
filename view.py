
def get_op():
    op = int(input("1 - Добавление нового студента \n 2 - Добавление предмета \n 3 - Добавление оценки ученику по предмету \n 4 - Показ списка учеников \n 5 - Показ листа оценок конкретного ученика \n 6 - выход\n"))
    return op


def input_student():
    name = input("Введите фамилию, имя: \n")
    return name


def input_less():
    less = input("Введите название предмета: \n")
    return less

def input_mark():
    name = input("Введите фамилию, имя: \n")
    less = input("Введите предмет: \n")
    mark = input("Введите оценку: \n")
    return name, less, mark

def print_mark():
    name = input("Введите имя для просмотра оценок: \n")
    return name