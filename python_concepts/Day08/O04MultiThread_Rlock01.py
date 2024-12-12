
# bus ticketing system

from threading import *
from time import sleep
mylock = RLock()

class Bus:

    def __init__(self, name, available_seats, rlock):
        self.available_seats = available_seats
        self.name = name
        self.rlock = rlock

    def reserve(self, need_seats):

        self.rlock.acquire()
        self.rlock.acquire()

        print("Available seats are :", self.available_seats)
        sleep(0.5)
        if self.available_seats >= need_seats:
            nm = current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats -= need_seats
        else:
            print("Sorry seats are fully booked.......")
        self.rlock.release()
        self.rlock.release()

b1 = Bus("KPN travels", 2, mylock)

t1 = Thread(target=b1.reserve, args=(1, ), name="Amit")
t2 = Thread(target=b1.reserve, args=(1, ), name="Geetha")

t1.start()
t2.start()
