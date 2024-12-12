"""
Advantage of using inheritance is we can get the data used in the thread
"""

from threading import Thread
from time import sleep

courses = ['Python', 'Data Science', 'ML', 'AI']

class MyCBT(Thread):

    def __init__(self, Flag):
        # execute the thread class ctor to start the necessary threads
        super().__init__()
        print("MyCBT Ctor......")
        self.student_offer = Flag

    def fastTrack(self):
        print("This is a fast track course.......")

    def run(self):
        a = 10
        b = 20
        self.fastTrack()

        if self.student_offer:
            print("Student offer is on........")

        for course in courses:
            print(f"{course} Joined......")
            sleep(2)
            print(f"{course} completed......")

        self.temp = a + b

t1 = MyCBT(False)
t1.start()              # child thread
sleep(10)             # putting the main thread to sleep for 10 secs
print(t1.temp)          # main thread


for i in range(3):
    print("hello world")