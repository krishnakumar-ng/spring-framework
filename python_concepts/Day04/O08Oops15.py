
class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print("getter called....")
        return self.__price

    @price.setter
    def price(self, prc):
        print("setter called....")
        self.__price = prc

    @price.deleter
    def price(self):
        print("deleter called.....")
        self.__price = 0


coke = Product(120)
print(coke.price)
coke.price = 105
print(coke.price)

del coke.price
print(coke.price)
