
def greet(msg):
    print(msg)

greet("Welcome....")

fun_name = greet

print(fun_name.__name__)
print(greet.__name__)

fun_name("Hello")

def bank_flow(fnc, arg):     # HOF
    print("-" * 60)
    print("logging into the server.....")
    fnc(arg)       # callback
    print("loggging out of the server.....")
    print("-" * 60)

def withdraw(amt):
    print(f"Amount {amt} debitted....")

def deposit():
    print("Amount Credited......")

def transfer():
    print("Amount Transferred.....")

bank_flow(withdraw, 5000)
# bank_flow(deposit)
# bank_flow(transfer)