# class Drob:
#     def __init__(self, cheslitel, znamenatel):
#         self.whole = 0
#         if cheslitel>znamenatel:
#             self.whole = cheslitel//znamenatel
#             self.cheslitel = cheslitel % znamenatel
#         else:
#             self.cheslitel = cheslitel
#         self.znamenatel = znamenatel
#
#     def __str__(self):
#         if self.whole == 0:
#             return f"{self.cheslitel} / {self.znamenatel}"
#         else:
#             return f"{self.whole}  {self.cheslitel}/{self.znamenatel}"
#
#     def add(self, cheslitel, znamenatel):
#         self.cheslitel = self.cheslitel*znamenatel + cheslitel*self.znamenatel
#         self.znamenatel = self.znamenatel*znamenatel
#         if cheslitel>znamenatel:
#             self.whole = self.whole + (self.cheslitel // self.znamenatel)
#             self.cheslitel = self.cheslitel % self.znamenatel
#
#     def add_drob(self, drob):
#         self.cheslitel = self.cheslitel * drob.znamenatel + drob.cheslitel * self.znamenatel
#         self.znamenatel = self.znamenatel * drob.znamenatel
#         if drob.cheslitel > drob.znamenatel:
#             self.whole = self.whole + (self.cheslitel // self.znamenatel)
#             self.cheslitel = self.cheslitel % self.znamenatel
#
#     def plus(self, drob):
#         new_cheslitel = self.cheslitel * drob.znamenatel + drob.cheslitel * self.znamenatel
#         new_znamenatel = self.znamenatel * drob.znamenatel
#         if self.whole != 0:
#             new_cheslitel = self.whole * new_znamenatel + new_cheslitel
#         return Drob(new_cheslitel, new_znamenatel)
#
#
#
# num1 = Drob(20,5)
# num2 = Drob(3,7)
# num1.add(3,7)
# # num2 = Drob(2,5)
# # print(num2)
# print(num1)
#
# num3 = Drob(20,5)
# num4 = Drob(3,7)
# num3.add(3,7)
# print(num3)
#
# num5 = Drob(20,5)
# num6 = Drob(3,7)
# num7 = num5.plus(num6)
# print(num7)

class Product:
    def __init__(self, dlinna):
        self.dlinna = dlinna

    def __add__(self, other):

        return Product(self.dlinna+other.dlinna)

    def __str__(self):
        return str(self.dlinna)

product = Product(55) + Product(8)
print(product)






