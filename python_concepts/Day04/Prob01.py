
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return str(self.salary)

    def __add__(self, other):
        return Employee("noName", self.salary + other.salary)



    # def __sub__(self, other):
    #     return Number(self.value - other.value)
    #
    # def __mul__(self, other):
    #     return Number(self.value / other.value)
    #
    # def __truediv__(self, other):
    #     return Number(self.value * other.value)
    #
    # def __floordiv__(self, other):
    #     return Number(self.value % other.value)
    #
    # def __mod__(self, other):
    #     return Number(self.value // other.value)


num1 = Employee("Jack", 1500)
num2 = Employee("Jill", 3000)
num3 = Employee("Peter", 2000)
num4 = Employee("John", 1000)

print("-" * 60)
print(f"num1 :{num1}")

print("-" * 60)
print(f"num2 :{num2}")

print("-" * 60)
print(num1 +  num2)

print("-" * 60)
print(num1 + num2 + num3 + num4)



"""
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(str(num1))
print(str(num2))
"""