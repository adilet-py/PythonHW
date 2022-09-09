# number = float(input("Введите вещественное число: "))
#
# sum = 0
# for i in str(number):
#     if i != ".":
#         sum += int(i)
#
# print(sum)




# number = int(input("Введите число: "))
#
# def mult(n):
#     if n == 1:
#         return 1
#     else:
#         return n * mult(n - 1)
#
# arr = []
# for i in range(1, number + 1):
#     arr.append(mult(i))
#
# print(f"Произведения чисел от 1 до {number}:  {arr}")





# k = int(input("Введите число k: "))
# s = 0
#
# arr = [(1+1/i)**i for i in range(1, k+1)]
# print(f"Полученная сумма последовательности (1+1/k)^k равна {round(sum(arr),2)}")




# n = int(input("Введите число N: "))
# pos = int(input("Сколько будет позиций?: "))
# nums = []
# for i in range(1, int(pos) + 1):
#     nums.append(int(input("Введите индекс: ")))
# arr = [i for i in range(-n, n+1)]
# print(arr)
# print(nums)
# mult = 1
# for i in range(0, pos):
#     mult *= arr[nums[i]]
# print(f"Произведение = {mult}")




import random
list = [random.randint(1, 10) for i in range(random.randint(1, 10))]
print(f"Исходный список:\n{list}")
random.shuffle(list)
print(f"Список после перемешивания:\n{list}")