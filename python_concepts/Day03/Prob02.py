import datetime
def timeTake(func):
    def helper(arg):
        start = datetime.datetime.now()
        func(arg)
        print(f"Function {func.__name__} is ended")
        end = datetime.datetime.now()
        print("Total time taken: ",end - start)

    return helper

@timeTake
def printFunction(n):
    lst = []
    for i in range(n):
        for j in range(1, i+1):
            lst.append(j ** 3)

printFunction(8000)