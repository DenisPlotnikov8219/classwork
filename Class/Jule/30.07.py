# Вывести строки
# file = open("Products.txt", "r")
# print(file.readlines())

#
# Вывести построчно
# file = open("Products.txt", "r")
# for i in file.readlines():
#     print(i, end="")

# file = open("Products.txt", "w")
# file.write("hnrtyj4tyjy")


# file = open("Products.txt", "a")
# file.write("hnrtyj4tyjy444444444444444444444")
#
# file = open("Products.txt", "w")
# file.writelines("ferf\n", "wefqwef\n", "qrgqerg\n")


# file = open("Products.txt", "w")
# text = ["ferf", "wefqwef", "qrgqerg"]
# for i in text:
#     file.write(i+"\n")
# file.close()


# Вывести и посчитать данные
# with open("Products.txt", "r", encoding="UTF-8") as file:
#     print(file.readlines())


# Вывести и посчитать данные
# with open("Products.txt", "r", encoding="UTF-8") as file:
#     for i in file.readlines():
#         ls = i.split(',')
#         if ls[2][-1:]=="\n": # обрезание \n
#             ls[2] = ls[2][:-1]
#         print(f"{ls[0]}: {int(ls[1])*int(ls[2])}")
#

# вести и поменять данные
# PATH = "Products.txt"
# def add_product(**kwargs):
#     products = dict()
#     with open(PATH, "r", encoding="UTF-8") as file:
#         for i in file.readlines():
#             ls = i.split(",")
#             products[ls[0]] = ls[1]
#         products[kwargs['name']] = f"{kwargs['prise']}\n"
#     with open(PATH, "w", encoding="UTF-8") as file:
#         for key, value in products.items():
#             file.write(f"{key},{value}")
#
#
# add_product(name="Котел", prise="16000")
# add_product(name="Мангал", prise="195000")
# add_product(name="Забор", prise="10000")

PATH = "Products.txt"
def add_product(**kwargs):
    products = dict()
    with open(PATH, "r", encoding="UTF-8") as file:
        for i in file.readlines():
            ls = i.split(",")
            products[ls[0]] = ls[1]
        products[kwargs['name']] = f"{kwargs['prise']}\n"
    with open(PATH, "w", encoding="UTF-8") as file:
        for key, value in products.items():
            file.write(f"{key},{value}")
# def sort_product():
#     products = dict()
#     with open(PATH, "r", encoding="UTF-8") as file:
#          for i in file.readlines():
#             ls = i.split(",")
#             products[ls[1]] = ls[1]


add_product(name="Котел", prise="16000")
add_product(name="Мангал", prise="195000")
add_product(name="Забор", prise="10000")