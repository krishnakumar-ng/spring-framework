
from collections import namedtuple

def Arithmetic(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    qout = x / y

    nmdTpl = namedtuple("Arithmetic", "s d p q")
    tpl = nmdTpl(s=sum, p=prod, d=diff, q=qout)
    return tpl

arith = Arithmetic(20, 8)
print(arith)
print(f"Sum  :{arith.s}")
print(f"Diff :{arith.d}")
print(f"Prod :{arith.p}")
print(f"Quot :{arith.q}")

