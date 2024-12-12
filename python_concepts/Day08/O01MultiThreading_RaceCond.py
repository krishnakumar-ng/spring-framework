
# bus ticketing system

from threading import *
from time import sleep
class Bus:

    def __init__(self, name, available_seats):
        self.available_seats = available_seats

    def reserve(self, need_seats):
        print("Available seats are :", self.available_seats)
        sleep(0.5)
        if self.available_seats >= need_seats:
            nm = current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats -= need_seats
        else:
            print("Sorry seats are fully booked.......")

b1 = Bus("KPN travels", 2)

t1 = Thread(target=b1.reserve, args=(1, ), name="Amit")
t2 = Thread(target=b1.reserve, args=(2, ), name="Geetha")

t1.start()
t2.start()
