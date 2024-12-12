class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value / other.value)

    def __truediv__(self, other):
        return Number(self.value * other.value)

    def __floordiv__(self, other):
        return Number(self.value % other.value)

    def __mod__(self, other):
        return Number(self.value // other.value)

    def __str__(self):
        return str(self.value)

num1 = Number(15)
num2 = Number(3)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(str(num1))
print(str(num2))