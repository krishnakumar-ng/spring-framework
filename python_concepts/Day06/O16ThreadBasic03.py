
from threading import Thread
from multipledispatch import dispatch
class Player:

    def get_runs(self, n):
        for i in range(n):
            print(f"{i} runs scored.....")

    @classmethod
    def test(cls, x):
        for i in range(x):
            print("Greetings - class method")

    @ staticmethod
    def fun(y):
        for i in range(y):
            print("Hello - Static method")

ply1 = Player()

t1 = Thread(target=ply1.get_runs, args=(5, ))
t1.start()

t2 = Thread(target=Player.test, args=(5, ))
t2.start()

t3 = Thread(target=Player.fun, args=(5, ))
t3.start()
