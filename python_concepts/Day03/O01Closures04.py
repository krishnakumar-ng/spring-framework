def fun(*args):
    print(args)

fun()
fun(1)
fun(1, 2)
fun(1, 3, 4)
print("-" * 60)

def sum(x, y):
    print(f"Adding {x} and {y}")
    return x + y

def diff(x, y):
    print(f"Subtracting {y} from {x}")
    return x - y

def log_details(fnc):
    logInfo = "Logging into Service....."

    def helper(*args):
        print(logInfo)
        print(fnc(*args))           # call back
        print("-" * 60)

    return helper

sum_logger = log_details(sum)
diff_logger = log_details(diff)

sum_logger(10, 20)
diff_logger(40, 26)


