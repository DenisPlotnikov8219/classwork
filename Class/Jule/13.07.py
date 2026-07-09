# st = input("Введите предложение: ")
# print(st.count(" ")+1)

import random
ls = []
n = int(input())
for i in range(n):
    ls.append(random.randint(1,9))
print(ls)


# def remove_all(ls,a):
#     i = 0
#     size = len(ls)
#     while i < size:
#         if ls[i] == a:
#             ls.remove(a)
#             size-=1
#         i+=1
# ls = [2,3,5,4,6,7,8,2,5,2,8]
# remove_all(ls,2)
# print(ls)

# def remove_all(ls,a):
#     i = 0
#     size = len(ls)
#     while i < size:
#         if ls[i] == a:
#             ls.pop(i)
#             size -= 1
#             i -= 1
#         i += 1
#
# ls = [2,3,5,4,6,7,8,2,5,2,8]
# ls.sort()
# remove_all(ls,2)
# print(ls)


