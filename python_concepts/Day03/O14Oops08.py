"""
we need to overload two operators
1. __eq__ (mandatory)
2. __gt__ (can be any comparison operator)

"""
from functools import total_ordering

@total_ordering             # all comparison operators will work
class Player:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"player initialized....")

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    # it works for not equal to (!=)
    def __eq__(self, other):
        return self.salary == other.salary

    # it works for less than also (<)
    def __gt__(self, other):
        return self.salary > other.salary



ply1 = Player("Kevin", 55000)
print(ply1)

print("-" * 60)

ply2 = Player("Peter", 50000)
print(ply2)

print("-" * 60)
# print(ply1 == ply2)             # compare the adresses by default

if ply1 != ply2:
    print("{}'s salary {} is NOT EQUAL to {}'s salary {}".format(ply1.name, ply1.salary, ply2.name, ply2.salary))
else:
    print("{}'s salary {} is EQUAL to {}'s salary {}".format(ply1.name, ply1.salary, ply2.name, ply2.salary))

print("-" * 60)

if ply1 < ply2:
    print("{}'s salary {} is LESS THAN  {}'s salary {}".format(ply1.name, ply1.salary, ply2.name, ply2.salary))
else:
    print("{}'s salary {} is NOT LESS THAN {}'s salary {}".format(ply1.name, ply1.salary, ply2.name, ply2.salary))

print("-" * 60)

print(ply1 >= ply2)