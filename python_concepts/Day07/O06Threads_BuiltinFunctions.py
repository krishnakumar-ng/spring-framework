
"""
count of current threads running
details of threads
"""

from threading import Thread, get_native_id, main_thread, active_count, enumerate
from time import sleep

def disp():
    print("ID :", get_native_id())
    print("Main Thread Details :", main_thread())
    for i in range(3):
        sleep(1)
        print("hello world")

def show():
    for i in range(3):
        sleep(2)
        print("Greetings......")

t1 = Thread(target=disp)
t2 = Thread(target=show)

print("Before :", t1.is_alive())
t2.start()
t1.start()

print("Native ID :", get_native_id(), "\n")

print("After :", t1.is_alive())
print("Number of threads :", active_count())

print("Thread Details :", enumerate())


