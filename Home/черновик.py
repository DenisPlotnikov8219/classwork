#
# нарисовать квадрат
# column = int(input())
# row = int(input())
# for i in range(row):
#     print("* " * column)

# нарисовать квадрат
# n=int(input())
# a = int(input())
# for i in range(a):
#     for j in range(n):
#         print("* ", end=" / ")
#     print()
#

# нарисовать квадрат цифрами
# n=int(input())
# a = int(input())
# k=1
# for i in range(a):
#     for j in range(n):
#         print(k, end=" / ")
#         k+=1
#     print()

# нарисовать квадрат формулами
# column = int(input())
# row = int(input())
# for i in range(1, row+1):
#     for j in range(1, column + 1):
#         print(f"{i} : {j}", end=" ")
#     print()

#
# нарисовать квадрат
# n = int(input("Введите число: "))
# for i in range(n):
#     for j in range(n):
#         print("* ", end=" ")
#     print()
#

# треугольник левый нижний угол
# n = int(input("Введите число: "))
# for i in range(n):
#     print("* "*(i+1))



# треугольник левый верхний угол
# n = int(input("Введите число: "))
# for i in range(n):
#     print("* "*(n-i))

# нарисовать ромб
# h = int(input("Введите высоту ромба: "))
# for x in range(h):
#     print(" " * (h - x), "*" * (2 * x + 1))
# for x in range(h - 2, -1, -1):
#     print(" " * (h - x), "*" * (2 * x + 1))

# треугольник правый нижний угол
# n = int(input("Введите число: "))
# for i in range(1, n+1):
#     print("  "*(n-i) + "* "*(i))

# треугольник правый верхний угол
# n = int(input("Введите число: "))
# for i in range(n, 0, -1):
#     print("  "*(n-i) + "* "*(i))


# нарисовать квадрат
# n = int(input("Введите число: "))
# print("* "*n)
# for i in range(n-2):
#     print("*  "+ "  "*(n - 2) + "*")
# print("* "*n)
#


# нарисовать треугольник вниз
# n = int(input("Введите число: "))
#
# for i in range((n+1)//2):
#     print("  "*i+"* "*(n-i*2))


# нарисовать треугольник
# n = int(input("Введите число: "))
# m = (2 * n) - 2
# for i in range(0, n):
#     for j in range(0, m):
#         print(end=" ")
#     m = m - 1
#     for j in range(0, i + 1):
#
#         print("*", end=' ')
#     print(" ")