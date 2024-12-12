
class Employee:

    def __init__(self, name, salary):
        self.name= name
        self.salary = salary
        self.tech = ['C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'Angular JS', 'React JS']

    def __str__(self):
        return "Name is {}\nSalary is {}".format(self.name, self.salary)

    def __iter__(self):
        return self.tech.__iter__()

    def append(self, item):
        self.tech.append(item)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, ind, val):
        self.tech[ind] = val

emp1 = Employee("Micheal", 8000)
print(emp1)

print("-" * 60)
print([e for e in emp1])

print("-" * 60)
emp1.append("Python")
print([e for e in emp1])

print("-" * 60)
x = emp1[4]
print(f"x :{x}")

print("-" * 60)
emp1[2] = "JSP"
print([e for e in emp1])


print("-" * 60)
print(emp1.name)

emp1.name = "Jackson"
print(emp1.name)
