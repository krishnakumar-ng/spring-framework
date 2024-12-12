
def add(x, y):
    return x + y

res = add(10, 20)
print(f"res :{res}")

a = add
print(a(185, 235))

print("-" * 60)
# lambdas

b = lambda x, y : x + y
print(b(453, 123))

"""
lambdas are best used with 
   a. map
   b. filter
   c. reduce
"""

print("map".center(60, "-"))
lst = list(range(1, 11))
print(f"lst :{lst}")

squares = list(map(lambda x : x ** 2, lst))
print(f"square :{squares}")

print("filter".center(60, "-"))
lst = list(range(1, 26))
print(f"lst :{lst}")

res = list(filter(lambda x : x % 3 == 0, lst))
print(f"res :{res}")

print("reduce".center(60, "-"))
from functools import reduce

lst = [9, 1, 5, 8, 10, 7, 2, 4, 6, 3]
print(f"lst :{lst}")

sum = reduce(lambda x, y : x + y, lst)
print(f"sum :{sum}")

grtst = reduce(lambda x, y : x if x > y else y, lst)
print(f"grtst :{grtst}")


