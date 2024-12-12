import threading
import time
from threading import Thread
from time import sleep

def fun(n, name):
    print(f"function executed.....{name}")
    sleep(n)
    print(f"function terminated......{name}")

st = time.perf_counter()

threads = []

for i in range(10):
    t = threading.Thread(target=fun, name="th-" + str(i), args=(2, "th-" + str(i)))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

et = time.perf_counter()
print(f"The total time take is :{round(et - st, 2)}")





