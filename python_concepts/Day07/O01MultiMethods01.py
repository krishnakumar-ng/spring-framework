
from multimethod import multimethod

@multimethod
def fun(x: int, y: int):
    return  x + y

@multimethod
def fun(x: float, y: float):
    return x + y

@multimethod
def fun(x: str):
    print(f"Greetings {x}")

print("-" * 60)
# fun with integers

res = fun(23, 78)
print(f"res :{res}")

print("-" * 60)
# fun with float

res = fun(45.8, 37.9)
print(f"res :{res}")

print("-" * 60)
fun("Sachin")
