
# bus ticketing system

from threading import *
from time import sleep
mylock = Lock()

class Bus:

    def __init__(self, name, available_seats, l):
        self.available_seats = available_seats
        self.name = name
        self.l = l

    def reserve(self, need_seats):
        self.l.acquire()
        print("Available seats are :", self.available_seats)
        sleep(0.5)
        if self.available_seats >= need_seats:
            nm = current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats -= need_seats
        else:
            print("Sorry seats are fully booked.......")
        self.l.release()

b1 = Bus("KPN travels", 2, mylock)

t1 = Thread(target=b1.reserve, args=(1, ), name="Amit")
t2 = Thread(target=b1.reserve, args=(1, ), name="Geetha")

t1.start()
t2.start()
