
def funLogger(fnc):

    def helper(*args):
        print("Logging into the service.....")
        res = fnc(*args)
        print("Logged out of the service.....")
        print("-" * 60)
        return res


    return helper

@funLogger
def add(x, y):
    print(f"Adding {x} and {y}")
    return x + y

@funLogger
def sub(x, y):
    print(f"Subtracting {y} from {x}")
    return x - y


res = add(34, 64)
print(res)

print("-" * 60)

res = sub(67, 24)
print(res)
