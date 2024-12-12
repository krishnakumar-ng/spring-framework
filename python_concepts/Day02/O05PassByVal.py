
def fun(x):
    print(f"inside :{x}")
    x = 500
    print(f"after :{x}")

n = 50
fun(n)

print(f"after call :{n}")
