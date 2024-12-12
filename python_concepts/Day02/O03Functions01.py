
def greet():
    print("Greetings Mr.Sachin Welcome to the event....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")

# city is called default argument, gname is called non default argument
def greetGstCty(gname, x,  city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.....")

greet()
print("-" * 60)

greetGst("Rahul")
greetGst("Sourav")

print("-" * 60)

greetGstCty("Rohit", 100)
greetGstCty("Hardik", 20)
greetGstCty("Rahul", 120,  "Bangalore")

print("-" * 60)
# args (order should be the same), kwargs(can be in any order)

def admission(name, dob, gender, city, contno, emailid, qlf):
    print(f"Name            :{name}")
    print(f"DOB             :{dob}")
    print(f"Gender          :{gender}")
    print(f"City            :{city}")
    print(f"Contact no.     :{contno}")
    print(f"Mail ID         :{emailid}")
    print(f"Qualification   :{qlf}")

# args
admission("Ruben", "20/07/1982", "Male", "Chennai", 238423700, "ruben@gmail.com", 'Btech')

print("-" * 60)
# kwargs
admission(qlf = 'MCA', gender="Female", city='Hyderabad', dob="19/02/1984", name="Tina", emailid="tina@gmail.com", contno=9234234223)

print("-" * 60)
# variable length arguments

def prodAll(*numbers):          # args - list or tuple
    print(numbers)
    print(*numbers)     # unpack
    prod = 1
    for number in numbers:
        prod *= number
    return prod

res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)

def getDetails(**details):      # **kwargs -> dictionary
    print(details)
    for k, v in details.items():
        print(k, "=>", v)


getDetails(name="Sachin", age=32, runs=79, oppn="WI", venue="Sabina Park")

print("-" * 60)
def multiplyMe(x, y):
    return x * y

a = 6
b = 8
print(f"The product of {a} and {b} is :{multiplyMe(a, b)}")

print("-" * 60)
# write a code with recursive to generate fibonacci series
def fibonacci(n):
    if(n == 0 or n == 1):
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

# iter = int(input("Enter the total numbers to be generated :"))
for x in range(8):
    print(fibonacci(x), end=" ")
print()

print("-" * 60)

def Arithmetic(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    qout = x / y
    return sum, diff, prod, qout

res = Arithmetic(20, 8)
print(f"res :{res}")

print("-" * 60)
def fun():
    # This is a comment
    "This is a doc string"
    print("Hello World")

fun()
print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)
    ----------

    i) if x and y are numbers then it returns the sum of the numbers
    ii) if x and y are strings then it returns the concatenated string
    iii) if x and y are of different data types then it throws an error
    """
    return x + y

print(fun1(45, 56))
print(fun1("hello ", "world"))

print("-" * 60)
help(fun1)
