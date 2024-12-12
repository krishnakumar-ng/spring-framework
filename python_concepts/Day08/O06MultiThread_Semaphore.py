
from threading import *
from time import sleep
semObj = BoundedSemaphore(3)

def disp(name):
    # calling the acquire method
    # will decrement the counter
    semObj.acquire()
    for i in range(5):
        print("Hello....")
        print(name)
        sleep(3)
    # calling the release method
    # will increase the counter val
    semObj.release()

# creating multiple threads
t1 = Thread(target = disp, args = ("Thread-1", ))
t2 = Thread(target = disp, args = ("Thread-2", ))
t3 = Thread(target = disp, args = ("Thread-3", ))
t4 = Thread(target = disp, args = ("Thread-4", ))
t5 = Thread(target = disp, args = ("Thread-5", ))

# calling the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
