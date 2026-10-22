# 1. Пользователь вводит 4 числа. Вывести на экран максимальное из них
# a1 = float(input("Ведите 1 число: "))
# a2 = float(input("Ведите 2 число: "))
# a3 = float(input("Ведите 3 число: "))
# a4 = float(input("Ведите 4 число: "))
# max = max(a1, a2, a3, a4)
# print(max)

# 2. Вывести все целые числа от а до b в порядке убывания
# a = int(input("Ведите 1 число: "))
# b = int(input("Ведите 2 число: "))
# for i in range(b, a - 1, -1):
#     print(i, end=" ")

# 3. Пользователь вводит сторону квадрата. Вывести на экран квадрат заполненый целыми числами с шагом 1, начиная с 5, в порядке возрастания
# n = int(input("Введите сторону квадрата: "))
# start = 5
# for i in range(n):
#     for j in range(n):
#         start += 1
#
#     print("\n ", (row))

# 4. Пользователь вводит символ, определить является ли он заглавной латинской буквой
# simvol = input("Введите символ: ")
#
# if 'A' <= simvol <= 'Z':
#     print("Да")
# # else:
#     print("Нет")

# 5. Создать одномерный список размером 8. Заполнить его целыми числами начиная от 0, по возрастанию, с шагом 3(циклом). Вывести список на экран
# list = []
# for i in range(8):
#     list.append(i * 3)
# print(list)

# 6. Создать двумерный массив, заполнить его случайными числами в диапазоне от a до b. Вывести на экран массив и среднее арифметическое всех элементов массива
# import random

#
# # 7. Найти наибольшее и наименьшее значение
# list = [num for row in massiv for num in row]
# min = min(list)
# max = max(list)
#
# print("\nРезультаты:")
# print(f"Наименьшее значение: {min}")
# print(f"Наибольшее значение: {max}")


# 8. Напишите функцию определяющую наличие переданного ей числа в одномерном списке чисел.
# def num_in_list(ls, num):
#     for i in ls:
#         if num == i:
#             return True
#         return False

# 9. Напишите

# def all_even_nums(ls):
#     result = []
#     for i in ls:
#         if i%2:
#             result.append(i)
#     return result

# 10.
# def get_column(ls, column_index):
#     result = []
#     for i in ls:
#         result.append(i[column_index])
#     return result


# 11.



# 12. Написать программу создавать студента, ...
# students = []
# students_marks=[]
# while True:
#     var = int(input('''
#     1 - Добавить студента,
#     2 - Вывести всех студентов из определенного класса,
#     3 - Удалить студента из списка,
#     4 - Добавить студенту оценку,
#     5 - Вывести всю информацию о студенте,
#     6 - Выводит всех студентов \n
#     '''))
#     if var == 1:
#         name = input("Bведите имя студента: ")
#         students.append(name)
#         students_marks.append([])
#     elif var == 2:
#         for i in range (len(students)):
#             print(f"{i+1}. {students[i]}: {students_marks[i]}")
#     elif var == 3:
#         index = int(input("Bведите номер студента для удаления: "))
#         if 1 <= index <= len(students):
#             students.pop(index-1)
#             students_marks.pop(index-1)
#         else:
#             print("Tакого студента нет")+
#     elif var == 4:
#         index = int(input("Bведите номер студента: "))
#         if index < 1 or index>len(students):
#             print("Hе корректный номер студента")
#         else:
#             mark = int(input("Bведите оценку: "))
#             students_marks[index-1].append(mark)
#     elif var == 5:
#             for i in range(len(students)):
#                 print(f"{i + 1}. {students[i]}: {students_marks[i]}")
#     elif var == 6:
#             for i in range(len(students)):
#                 print(f"{i + 1}. {stude