
class Test:

    def fun(self, a, b):
        return a + b

    def fun(self, a, b, c):
        print(a, b, c)


t1 = Test()
t1.fun(10, 20)
t1.fun(1, 2, "hello")
