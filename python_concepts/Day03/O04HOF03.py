
def funLogger(fnc):
    def helper():
        print("Logging into a service.....")
        fnc()
        print("Logging out of the service.....")
        print("-" * 60)

    return helper


def normal_fun():
    print("I should be called normal.....")


funLogger(normal_fun)       # no output
print("-" * 60)

funLogger(normal_fun)()
print("-" * 60)

res_fun = funLogger(normal_fun)
# res_fun()
print(res_fun.__name__)
print("-" * 60)

normal_fun = funLogger(normal_fun)
print(normal_fun.__name__)
normal_fun()

print("-" * 60)

@funLogger          #basic_fun = funLogger(basic_fun)
def basic_fun():
    print("I should be called as BASIC.....")

basic_fun()

print("-" * 60)
print(basic_fun.__name__)
