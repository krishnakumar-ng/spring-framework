
from threading import *
from time import sleep

rlock = RLock()

def get_first_line():
    rlock.acquire()
    print("Code fetching first file")
    rlock.release()

def get_second_line():
    rlock.acquire()
    print("Code fetching second file")
    rlock.release()

def main():
    rlock.acquire()

    get_first_line()
    get_second_line()

    rlock.release()

t1 = Thread(target=main)
t1.start()
