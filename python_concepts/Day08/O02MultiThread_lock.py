"""
Join - will block a thread until the target thread finishes

lock - will block the until the lock is released
"""
from threading import *
from time import sleep

mylock = Lock()

def task(mylock, msg):
    mylock.acquire()
    for i in range(5):
        print(msg)
    sleep(3)
    mylock.release()

t1 = Thread(target=task, args=(mylock, "Hello World"))
t2 = Thread(target=task, args=(mylock, "Greetings....."))

t1.start()
t2.start()


