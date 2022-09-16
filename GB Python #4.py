# from math import pi
#
# d =  int(input("Введите точность числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')



# num = int(input("Введите число: "))
# i = 2 # первое простое число
# list = []
# old = num
# while i <= num:
#     if num % i == 0:
#         list.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {list}")



#list = list(map(int, input("Введите числа через пробел:\n").split()))
#print(f"Исходный список: {list}")
#new_list = []
#[new_list.append(i) for i in list if i not in new_list]
#print(f"Список из неповторяющихся элементов: {new_list}")


# import random
#
#
# def write_file(st):
#     with open('file.txt', 'w') as data:
#         data.write(st)
#
#
# def rnd():
#     return random.randint(0, 101)
#
#
# def create_mn(k):
#     list = [rnd() for i in range(k + 1)]
#     return list
#
#
# def create_str(sp):
#     list = sp[::-1]
#     wr = ''
#     if len(list) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(list)):
#             if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
#                 wr += f'{list[i]}x^{len(list) - i - 1}'
#                 if list[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(list) - 2 and list[i] != 0:
#                 wr += f'{list[i]}x'
#                 if list[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(list) - 1 and list[i] != 0:
#                 wr += f'{list[i]} = 0'
#             elif i == len(list) - 1 and list[i] == 0:
#                 wr += ' = 0'
#     return wr
#
#
# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))


import random


# запись в файл
def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)


# создание случайного числа от 0 до 100
def rnd():
    return random.randint(0, 101)


# создание коэффициентов многочлена
def create_mn(k):
    lst = [rnd() for i in range(k + 1)]
    return lst


# создание многочлена в виде строки
def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0 or lst[i + 2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i + 1] != 0 or lst[i + 2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


# получение степени многочлена
def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


# получение коэффицента члена многочлена
def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


# разбор многочлена и получение его коэффициентов
def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1  # степень
    ii = l - 1  # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst


# создание двух файлов

k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("file_1.txt", create_str(koef1))
write_file("file_2.txt", create_str(koef2))

# нахождение суммы многочлена

with open('file_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll, mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll, mm):
        lst_new.append(lst2[i])
write_file("file_summa.txt", create_str(lst_new))
with open('file_summa.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")