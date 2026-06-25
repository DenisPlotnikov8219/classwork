# st = [4,5,3,4,3,4,2,4]
# summa = 0
# for i in range(8):
#     summa+=st[i]
# print(f"summa={summa}")

    # print(st[i], end="")

# print(st[7])
# print(st[0])
# print(st[0]+st[1]+st[2]+st[3]+st[4]+st[5]+st[6]+st[7]+st[8]/8)

#
# вывести четные
# st = [4,5,3,4,3,4,2,4]
# for i in range(8):
#     if st [i]%2==0:
#         print(st[i])


# вывести слева на прав
# st = [4,5,3,4,3,4,2,4]
#
# for i in range(7, -1, - 1):
#         print(st[i], end=" ")


# все 5 уменьшить на1
# st = [4,5,3,4,3,4,2,4]
#
# for i in range(len(st)):
#     if st[i]%5 == 1:
#         st[i] -= 1
# print(st)


# вывести индеус четных
# st = [4,5,3,4,2,4,5,3]
# for i in range(8):
#     if st[i] % 2 == 0:
#         print(i , end=" ")
#

# st = [4,5,3,4,22,4,5,3]
#
# max = [st[0], 0]
# min = [st[0], 0]
# for i in range(1,len(st)):
#     if st[i] < min[0]:
#         min = [st[i], i]
#     if st[i] > max[0]:
#         max = [st[i],i]
# print(f"максимальное число {max[0]} с индексом {max[1]}")
# print(f"минимальное число {min[0]} с индексом {min[1]}")

# st = [4,5,3,4,22,4,5,3]
#
# for i in st:
#     if i%2 == 0:
#         print(i, end=" ")

# st = [4,5,3,4,22,4,5,3]
#
# sum=0
# for i in st:
#     sum+=st[i]
# print(sum)


# st = [4,5,3,4,22,4,5,3]
# sum = 0
# for i in range(len(st)-1,-1,-1):
#     print(st[i])

#
# ls = [23,5,3,5,2.72,3]
# for i in range(len(ls)):
#
#     flag=True
#     for j in range (len(ls)):
#         if i == j:
#             continue
#         if ls[i] == ls[j]:
#             print(ls[i], end=" ")
#             break
#
# st = [23, 5, 3, 5, 2, 72, 3]
# for i in range(len(st)):
#     flag = True
#     for j in range(i + 1, len(st)):
#         if i == j:
#             continue
#         if st[i] == st[j]:
#             flag = False
#             break
#
#     if not flag:
#         print(st[i], end=" ")

st = [23, 5, 3, 5, 2, 72, 3]
sl = [23, 5, 3, 5, 2, 72, 3]
flag = True
if len(st) == len(sl):
    for i in range(len(st)):
        if st[i] == sl[i]:
            flag = True
        else:
            flag = False
    if flag:
        print("ravn")
    else: print("ne ravn")
else:
    print("ne ravn")


