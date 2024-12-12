
import time
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor, as_completed

def doJob(secs):
    print(f"going to sleep for {secs} seconds.....{current_thread().name}")
    time.sleep(secs)
    print(f"Just woke up from sleep........{current_thread().name}")
    return "task completed"

st = time.perf_counter()
with ThreadPoolExecutor() as executor:
    secs = [6, 5, 4, 3, 2, 1]
    results = executor.map(doJob, secs)

    for result in results:
        print(result)

et = time.perf_counter()

print(f"The total time taken :{et - st}")