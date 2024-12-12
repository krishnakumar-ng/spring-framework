import time
from threading import Thread
from time import sleep

def fun():
    print("function executed.....")
    sleep(2)
    print("function terminated......")

st = time.perf_counter()

t1 = Thread(target=fun)
t2 = Thread(target=fun)
t3 = Thread(target=fun)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

et = time.perf_counter()
print(f"The total time taken to execute :{round(et - st, 2)}")
