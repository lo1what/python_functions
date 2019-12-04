'''Задание - 1
Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
Функция должна возвращать строку вида
"Василий, 21 год(а), проживает в городе Москва"'''


def user_map(name, age, city):
    '''name(str), age(str), city(str) --> str'''

    str_user = f'{name}, {age} год(а), проживает в городе {city}'
    return str_user


print(user_map('Василий', '21', 'Москва'))

'''Задание - 2
Создайте функцию, принимающую на вход 3 числа, и возвращающую
наибольшее из них.'''


def max_number(*args):
    '''numbers (int/float) --> max (int/float)'''

    max_num = 0
    for arg in args:
        if arg > max_num:
            max_num = arg
    return max_num


print(max_number(9, 11, 13, 43, 10.5, 50.5, 90, 11))

