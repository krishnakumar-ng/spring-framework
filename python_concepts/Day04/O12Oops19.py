
class Animal:

    def __init__(self):
        self.a = 10
        print("Animal Ctor.....")

    def eat(self):
        print("Animals eat.....")

    def fun(self):
        print("fun method of Animal class")

class Person:

    def __init__(self):
        self.p = 20
        print("Person Ctor......")

    def walk(self):
        print("Person walks.......")

    def fun(self):
        print("fun method of Person class")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()          # calls the parent
        Person.__init__(self)
        self.g = 30
        print("Girl Ctor......")

    def talk(self):
        print("Girls talk......")


tina = Girl()
tina.eat()
tina.walk()
tina.talk()

print("-" * 60)
tina.fun()

print("-" * 60)
print(tina.__dict__)
