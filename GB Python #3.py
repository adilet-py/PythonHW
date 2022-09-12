# def sum_odd_index(list):
#     s = 0
#     for i in range(len(list)):
#         if i % 2 != 0:
#             s += list[i]
#     print(f"Сумма равна: {s}")
#
# list = list(map(int, input("Введите числа через пробел:\n").split()))
# sum_odd_index(list)



# def mult_list(list):
#     l = len(list)//2 + 1 if len(list) % 2 != 0 else len(list)//2
#     new_list = [list[i]*list[len(list)-i-1] for i in range(l)]
#     print(new_list)
#
# list = list(map(int, input("Введите числа через пробел:\n").split()))
# mult_list(list)



# list = list(map(float, input("Введите числа через пробел:\n").split()))
# new_list = [round(i%1,2) for i in list if i%1 != 0]
# print(max(new_list) - min(new_list))



# s = ""
# n = int(input("Введите число:\n"))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)




n = int(input('Введите число: '))

def fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = fibonacci(n)
print(fibonacci(n))
print(fibo_nums.index(0))