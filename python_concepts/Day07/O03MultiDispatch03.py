
from multipledispatch import dispatch

class Test:

    @dispatch(int, int)
    def fun(self, x: int, y: int):
        return x + y
    @dispatch(str, str)
    def fun(self, a: str, b: str):
        return a + " " + b

t1 = Test()
print("-" * 60)
res = t1.fun(34, 23)
print(f"res :{res}")

print("-" * 60)
res = t1.fun("Hello", "World")
print(f"res :{res}")