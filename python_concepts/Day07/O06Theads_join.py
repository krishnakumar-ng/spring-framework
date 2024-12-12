
from threading import Thread
from time import sleep

def disp():
    for i in range(5):
        print("Hello World")

def show():
    for i in range(5):
        print("Greetings....")

t1 = Thread(target=disp)
t2 = Thread(target=show)

t2.start()
t2.join()

t1.start()
t1.join()

for i in range(3):
    print(f"Main Thread - {i}")