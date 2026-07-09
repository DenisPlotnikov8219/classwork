# a = (1,2,3,4,5,6)
# a.index()
#
# a = {'a', 'b', 'c'}
# print('b' in a)

# a = {'a', 'b', 'c', 'd'}
# b = {'a1', 'b', 'c1', 'd'}
# print(a.isdisjoint(b))

# a = {'a', 'b', 'c', 'd'}
# b = {'a1', 'b', 'c1', 'd'}
# print(a==b)

# a = {'a', 'b', 'c', 'd'}
# b = {'a1', 'b', 'c1', 'd1'}
# print(a.union(b))
#


# import random
#
#
# def create_random_set(size):
#     n1 = []
#     while size > 0:
#
#         num = random.randint(1,9)
#         if num not in n1:
#             n1.append(num)
#             size -= 1
#
#     return n1
# s1 = set(create_random_set(5))
# s2 = set(create_random_set(9))
# print(s1)
# print(s2)
# print(len(s1.intersection(s2)))

# products = {
#     "Category": "Продукты",
#     "Price": 1200.50,
#     "Count": 120,
#     "Colors": ["Красный", "Синий"]
# }
# for i in products.keys():
#     print(f"{i} - {products[i]}")

# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
# for key in users:
#     print(f"Phone: {key}  User: {users[key]} ")

# users = {"+1111111": "Tom", "+3333333": "Bob"}
#
# users2 = {"+2222222": "Sam", "+6666666": "Kate"}
# users.update(users2)
#
# print(users)
# print(users2)

# products = {
#     "Category": "Продукты",
#     "Price": 1200.50,
#     "Count": 120,
#     "Colors": ["Красный", "Синий"]
# }
# products["Category"]="Коврик"
#     print(f"Phone: {key}  User: {users[key]} ")

import random

def show_dikt():
    for i in products.keys():
        print(f"{i} - {products[i]}")

disciplines = ["eng", "mat", "rus", "lit"]
st = {}
def disciplines_ocenka():
    st = {}
    for i in disciplines:
        st[i] = []
        for j in range(random.randint(3,9)):
            st[i].append(random.randint(2,5))
    return st
def avg(list):
    sum = 0
    for i in list:
        sum += 1
    return sum/len(list)
def best_disciplines_name(st):
    max = 0
    disc_name = "unname"
    for i in st.keys():
        avg_mark = avg(st[i])
        if max < avg_mark:
            max = avg_mark
            disc_name = i
    return disc_name
def big_disciplines_name(st):
    max = 0
    disc_name = "unname"
    for i in st.keys():
        avg_mark = len(st[i])
        if max < avg_mark:
            max = avg_mark
            disc_name = i
    return disc_name

def big_disciplines_more(st):
    disc_name = "unname"
    for i in st.keys():
        avg_mark = avg(st[i])
        if max < avg_mark:
            max = avg_mark
            disc_name = i
    return disc_name



st1 = disciplines_ocenka()
show_dikt(st1)


