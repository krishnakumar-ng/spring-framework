"""
submit():
Submits a single task to the thread pool and returns a Future object representing the task.

result():
Blocks until the task associated with the Future object completes and returns the result.

as_completed():
Returns an iterator that yields Future objects as they complete, allowing you to process results as they become available.

"""
import time
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor, as_completed

def doJob(secs):
    print(f"going to sleep for {secs} seconds.....{current_thread().name}")
    time.sleep(secs)
    print(f"Just woke up from sleep........{current_thread().name}")

st = time.perf_counter()
with ThreadPoolExecutor() as executor:
    secs = [6, 5, 4, 3, 2, 1]
    results = [executor.submit(doJob, sec) for sec in secs]

    for res in as_completed(results):
        print(res.result())

et = time.perf_counter()

print(f"The total time taken :{et - st}")