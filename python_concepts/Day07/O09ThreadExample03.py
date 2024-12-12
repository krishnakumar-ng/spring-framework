
import time
from threading import current_thread
import concurrent.futures

def doJob(secs):
    print(f"going to sleep for {secs} seconds.....{current_thread().name}")
    time.sleep(2)
    print(f"Just woke up from sleep........{current_thread().name}")

st = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    thrd1 = executor.submit(doJob, 2)
    thrd2 = executor.submit(doJob, 2)
    thrd3 = executor.submit(doJob, 2)

    thrd1.result()
    thrd2.result()
    thrd3.result()

et = time.perf_counter()
print(f"Total time taken to execute :{et - st}")
