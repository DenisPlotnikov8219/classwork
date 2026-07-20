
# a = int(input("Введите начальное число диапазона:"))
# b = int(input("Введите конечное число диапазона:"))
#
# s = a
# sum = 0
#
# while s <= b:
#     sum += s
#     s += 1
#
# print(f"Сумма чисел от {a} до {b} равна: {sum}")


#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# while b!= 0:
#  o = b
#  b = a% b
#  a = o
#
# print("Наибольший общий делитель*:", a)

# a = int(input("Введите число: "))
# if a <= 0:
#     print("Bведите положительное число.")
# else:
#     d = 1
#     print(f"Делители числа {a}: ")
#
# while d <= a:
#     if a % d == 0:
#         print(d)
#     d += 1
#
#
#
# a = int(input("Введите целое число: "))
#
# if a == 0:
#     col = 1
# else:
#
#     a = abs(a)
#     col = 0
#
#     while a > 0:
#         a = a // 10
#         col += 1
#
# print(f"Количество цифр в числе: {col}")





count_positive = 0
count_negative = 0
count_zero = 0
count_even = 0
count_odd = 0

num_count = 0

print("Введите 10 чисел:")

while num_count < 10:

    number = float(input(f"Число {num_count + 1}:"))


    if number > 0:
        count_positive += 1
    elif number < 0:
        count_negative += 1
    else:
        count_zero += 1

    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

    num_count += 1

print("\nСтатистика: ")
print(f"Положительных чисел: {count_positive}")
print(f"Отрицательных чисел: {count_negative}")
print(f"Нулей: {count_zero}")
print(f"Чётных чисел: {count_even}")
print(f"Нечётных чисел: {count_odd}")

