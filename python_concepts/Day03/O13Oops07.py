# magic methods

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"player initialized....")

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}"


ply1 = Player("Sachin", 20)
# ply1.get_details()

print("-" * 60)
print(str(ply1))

print("-" * 60)
print(ply1.__str__())

print("-" * 60)
print(ply1)         # in will implicitly call __str__ method