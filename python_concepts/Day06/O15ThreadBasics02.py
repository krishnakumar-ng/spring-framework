
from threading import current_thread

print(current_thread())

print("Main Thread Name :", current_thread().name)
print("PID :", current_thread().ident)
print("Thread Status :", current_thread().is_alive())
