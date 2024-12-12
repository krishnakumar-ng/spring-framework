
class Employee:

    def __init__(self, name, salary):
        self.name= name
        self.salary = salary
        self.tech = ['C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'Angular JS', 'React JS']

    def __str__(self):
        return "Name is {}\nSalary is {}".format(self.name, self.salary)

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)
        # return self.tech.__iter__()

    def append(self, item):
        self.tech.append(item)

emp1 = Employee("Jack", 65000)
print(emp1)

print("-" * 60)
print([e for e in emp1])

print("-" * 60)
print(len(emp1))

print("-" * 60)
emp1.append("Python")
print([e for e in emp1])

