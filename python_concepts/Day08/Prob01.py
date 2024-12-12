
# bus ticketing system

from threading import *
from time import sleep
# mylock = RLock()
mylock = BoundedSemaphore(2)

class Bus:

    def __init__(self, name, available_seats, mylock):
        self.available_seats = available_seats
        self.name = name
        self.mylock = mylock

    def reserve(self, need_seats):

        self.mylock.acquire()

        print("Available seats are :", self.available_seats)
        sleep(0.5)
        if self.available_seats >= need_seats:
            nm = current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats -= need_seats
        else:
            print("Sorry seats are fully booked.......")
        sleep(1)
        self.mylock.release()

b1 = Bus("KPN travels", 4, mylock)

t1 = Thread(target=b1.reserve, args=(1, ), name="Amit")
t2 = Thread(target=b1.reserve, args=(1, ), name="Geetha")
t3 = Thread(target=b1.reserve, args=(1, ), name="Ravi")
t4 = Thread(target=b1.reserve, args=(1, ), name="Sita")

t1.start()
t2.start()
t3.start()
t4.start()