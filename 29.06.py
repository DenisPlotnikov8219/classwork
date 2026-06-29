# marks = [2, 3, -4, 3, 8, -9, 9, 0, -4 ]
# student = [4, "Иван", 4.5]

# вывести все отрицательные
# marks = [2, 3, -4, 3, 8, -9, 9, 0, -4 ]
# for i in marks:
#     if i<0:
#         print(i, end= " ")


# делать все положительные
# marks = [2, 3, -4, 3, 8, -9, 9, 0, -4 ]
# for i in marks:
#     if i<0:
# for i in range (len(marks)):
#     if marks[i]<0:
#         marks[i]*=-1
#         print(i, end=" ")

# вывести задам наперед
# marks = [2, 3, -4, 3, 8]
# for i in range (len(marks)//2):
#     marks[i], marks[len(marks)-(i+1)]=marks[len(marks)-(i+1)], marks[i]
# print(marks)

# Проверить равны ли имена
# name = ["Вася", "Вася", "Вазя"]
# flag = True
# for i in range (1, len(name)):
#     if len(name[i])!=len(name[0]):
#         flag = False
#         break
# print(flag and "Да" or "Нет")

# Вывести все имена заканчивающиеся на а
# name = ["Вася", "Вася", "Вазя", "Ева", "Ольга", "Паша"]
# for i in name:
#     if i[len(i)-1]=="а":
#         print(i, end=" ")
# print()

# name = [[2,3,4,3],
#          [3,4,3,5],
#          [4,4,4,5]]
# for i in range(len(name)):
#     print(f"Студент {i+1}: ", end=" ")
#     summa=0
#     for j in name[i]:
#         summa+=j
#         print(j, end=" ")
#     print(" I ", summa/len(name[i]))

# name = [[2,3,4,3],
#          [3,4,3,5]]
# for i in range(len(name)):
#     summa=0
#     for j in name[i]:
#         summa+=j
#         print(j, end="\t")
#     print(" I ", summa)
# print("---------------------------")
# result = 0
# for i in range(len(name[0])):
#     summa = 0
#     for j in range(len(name)):
#         summa+=name[j][i]
#     print(summa, end="\t")
#     result+=summa
#
# print(" I ", result)
