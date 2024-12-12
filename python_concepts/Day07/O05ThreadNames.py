"""
thread identifier - ident

native identifier - same as ident name is native_id

NOTE - native_id and ident will have the same values but completely different identifiers

PID - process id - main program
"""

from threading import Thread, current_thread
import os

def disp():
    for i in range(5):
        print("Hello World")

def show():
    for i in range(4):
        print("Welocome....")

t1 = Thread(target=disp)
t2 = Thread(target=show)

print(t1.name)
print(t2.name)

t1.name = "MyThread01"
print(t1.name)

print("-" * 60)
# deprecated -  getname() - now it is name
# print(t1.getName())
# print(t2.getName())

print(current_thread().name)
current_thread().name = "MyMainThread"
print(current_thread().name)

print("-" * 60)
t1.start()
print(t1.ident)
print(t1.native_id)
print(os.getpid())

print("-" * 60)
print(current_thread().ident)

