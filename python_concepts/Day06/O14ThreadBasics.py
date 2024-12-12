
# importing a thread class

from threading import Thread

def disp(n, msg):
    for i in range(n):
        print(msg)

t1 = Thread(target=disp, kwargs = {'n': 5, 'msg':"hello world"})

t1.start()

# main thread
for i in range(4):
    print("welcome....")
