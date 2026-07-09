
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# sum=0
# for i in range(a, b+1, 1):
#     sum+=i
# print(sum)


# n = int(input("Введите число: "))
# if n<0:
#     for i in range(0, n-1, -1):
#         print(i, end=" ")
# if n>0:
#     for i in range(0, n+1, 1):
#         print(i, end=" ")

# fact=



# max = int(input("Введите число: "))
# for i in range(4):
#     a = int(input())
#     if a>max:
#         a=max
# print(max)

#
# n = int(input("Введите число: "))
# for i in range(1, n, 1):
#     print(i, end=" ")

# n=int(input())
# print("* "*n)


# column = int(input())
# row = int(input())
# for i in range(row):
#     print("* " * column)

# n=int(input())
# a = int(input())
# for i in range(a):
#     for j in range(n):
#         print("* ", end=" / ")
#     print()
#
# n=int(input())
# a = int(input())
# k=1
# for i in range(a):
#     for j in range(n):
#         print(k, end=" / ")
#         k+=1
#     print()


# column = int(input())
# row = int(input())
# for i in range(1, row+1):
#     for j in range(1, column + 1):
#         print(f"{i} : {j}", end=" ")
#     print()

# n = int(input("Введите число: "))
# for i in range(n):
#     for j in range(n):
#         print("* ", end=" ")
#     print()
#
# n = int(input("Введите число: "))
# for i in range(n):
#     print("* "*(i+1))
#
# n = int(input("Введите число: "))
# for i in range(n):
#     print("* "*(n-i))

# n = int(input("Введите число: "))
# for i in range(1, n+1):
#     print("  "*(n-i) + "* "*(i))

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
