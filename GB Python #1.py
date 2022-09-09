# num = int(input())
#
# if 6 <= num <= 7:
#     print("Да")
# elif 0 < num < 6:
#     print("Нет")
# else:
#     print("нет такого дня недели")



# a = []
# for i in range(3):
#     a.append(input(f"Введите значение: "))
#
# left = not (a[0] or a[1] or a[2])
# right = not a[0] and not a[1] and not a[2]
#
# if left == right:
#     print("Выражение истинно")
# else:
#     print("Выражение ложно")




# x = int(input("Введите Х: "))
# y = int(input("Введите Y: "))
# if(x == 0) or (y == 0):
#     print("Введите отличные от 0 числа")
# result = 4
# if x > 0 and y > 0:
#     result = 1
#     print(f"Точка находится в {result} четверти")
# elif x < 0 and y > 0:
#     result = 2
#     print(f"Точка находится в {result} четверти")
# elif x < 0 and x < 0:
#     result = 3
#     print(f"Точка находится в {result} четверти")



# num = int(input("Введите номер четверти: "))
# if num < 1 or num > 4:
#     print("Введите номер четверти(1-4)")
# if(num == 1):
#     print("0 < x < +00")
#     print("0 < y < +00")
# elif(num == 2):
#     print("-00 < x < 0")
#     print("0 < y < +00")
# elif(num == 3):
#     print("-00 < x < 0")
#     print("-00 < y < 0")
# elif(num == 4):
#     print("0 < x < +00")
#     print("-00 < y < 0")




x1 = int(input("Введите x1: "))
x2 = int(input("Введите x2: "))
y1 = int(input("Введите y1: "))
y2 = int(input("Введите y2: "))
length = ((y1 - x1) ** 2 + (y2 - x2) ** 2) ** (0.5)
print(f"Длина отрезка равна {length}")