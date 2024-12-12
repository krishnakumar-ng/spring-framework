
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.age = 1

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):
    def __init__(self):         # override the parent class Ctor
        super().__init__()      # calls the parent class Ctor
        self.weight = '1kg'
        print("Bird Ctor.....")

    def fly(self):
        print("Birds Fly.....")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()
print(cuckoo.__dict__)