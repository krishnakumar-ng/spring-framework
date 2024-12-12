"""
self - will have the name of the object that called the method

ply1.get_details()

def get_detials(ply1)
    print(ply1.name)
    print(ply1.age)

"""
class Player():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Virat", 34)
ply1.get_details()

print("-" * 60)

ply2 = Player("Rohit", 33)
ply2.get_details()

print("-" * 60)
print(f"ply1 :{ply1.__dict__}")
print(f"ply2 :{ply2.__dict__}")

print("-" * 60)
ply2.runs = 150
print(f"ply1 :{ply1.__dict__}")
print(f"ply2 :{ply2.__dict__}")




