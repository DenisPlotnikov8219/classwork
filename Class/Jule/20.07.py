# Рекурсия
# def fact(n):
#     if n > 1:
#         return n*fact(n-1)
#     else:
#         return 1
# print(fact(5))
# Сортировка
# ls = [5,8,89,565,45,695,12,23]
# ls.sort()
# print(ls)

#
#
# Бинарный поиск
# def binary_search(ls, n, min_i = 0, max_i = -1):
#     if max_i == -2: max_i = len(ls)-1
#     if min_i > max_i: return False
#     current_i = (max_i+min_i)//2
#     if n == ls[current_i]: return True
#     elif n < ls[current_i]: binary_search(ls, n, min_i, current_i-1)
#     else: return binary_search(ls, n,  current_i+1, max_i)
#
#
#
# ls = [5, 8, 12, 23, 45, 89, 565, 695]
# print(ls)
# n = 23
# min_i = 0
# max_i = len(ls)-1
#
# while True:
#     current_i = (max_i+min_i)//2
#     if min_i > max_i:
#         print("No")
#         break
#     if n == ls[current_i]:
#         print("yes")
#         break
#     elif n < ls[current_i]:
#         max_i = current_i-1
#     elif n > ls[current_i]:
#         min_i = current_i+1

# Выводит из строки все слова из трех букв
# str = "функция которая дан ф на перрвом не"
#
# def little_words(str):
#     words = str.split(" ")
#     result = set()
#     for i in words:
#         if len(i) < 3:
#             result.add(i)
#     return result
# print(little_words(str))

# Возвращает все повторяющиеся элементы 2 списков
#
# list1 = [4,5,6,5,54,5,6,4]
# list2 = [45,789,564,4,6]
# def list_equality(list1, list2):
#     result = set()
#     for i in list1:
#         if i in list2:
#             result.add(i)
#     return result
# print(list_equality(list1, list2))
# print(set(list1).intersection(set(list2)))



