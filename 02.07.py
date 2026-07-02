# import random
#
# a = int(input("Введите число "))
# b = int(input("Введите число "))
#
# list1 = [0,0,0,0,0,0,0,0,0,0,0,0]
# for i in range(len(list1)):
#     list1[i] = random.randint(a,b)
# print(list1)
# print(max(list1))
#
# max_index = 0
#
# print(f"Значение:{max(list1)}  Индекс: {max_index}  ")
#
# list2 = [0,0,0,0,0,0,0,0,0,0,0,0]
# n = 0
# for i in range(len(list1)):
#     if list1[i]%2==0:
#         list2[n]=list1[i]
#         n+=1
# print(list1)
# print(list2)
# list2 = [0,0,0,0,0,0,0,0,0,0,0,0]
# n = 0
# for i in range(len(list1)):
#     if list1[i]%2!=0:
#         list2[n]=list1[i]
#         n+=1
# print(list1)
# print(list2)


# def show_start():
#     print("---Начало программы----")
# show_start()
# print("n1")
# show_start()
# print("n2")
# show_start()
# print("n3")
# show_start()
# print("n4")

# def maximum(list1):
#     max=list1[0]
#     for i in range (len(list1)):
#         if list1[i]>max:
#             max=list1[i]
#     return max
#
#
#
# student = [2,4,3,5,86,5,2]
# print(maximum(student))
#
import random
# def generate_rand(list1):
#     for i in  range(len(list1)):
#         list1[i]=random.randint(1,99)
#     print(i)
#     list1 = school
#
# print(range(list1(i)))

# def aver(list1):
#     summ=0
#     for i in list1:
#         summ+=1
#         return summ/len(list1)
school = [[2,3,5,2,5,4,6,3],
          [2,4,5,3],
          [2,5,4,4,4,4,4]]
# summa=0
# for i in school:
#     summa+=aver(i)
# print(summa/len(school))
# def maximum(list1):
#     max=list1[0]
#     for i in range(len(list1)):
#         if list1[i]>max:
#             max=list1[i]
#     return max
# print(i)

maximum = 0
for i in range(len(school)):
    if max < maximum(school[i]):
        max = school[i]
        index_max = i
print(index_max[i])