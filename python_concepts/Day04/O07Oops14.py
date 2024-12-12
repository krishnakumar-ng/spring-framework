
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        print("getter called...")
        return self.__price

    def set_price(self, prc):
        print("setter called.....")
        self.__price = prc

    def del_price(self):
        print("deleter called......")
        self.__price = 0

    price = property(get_price, set_price, del_price)

pepsi = Product(85)
print(pepsi.price)
pepsi.price = 50
print(pepsi.price)

del pepsi.price
print(pepsi.price)

