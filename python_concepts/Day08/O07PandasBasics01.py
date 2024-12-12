
import pandas as pd

x = [1, 2, 3, 4, 5]
print(f"x :{x}")

mySrs = pd.Series(x)
print(mySrs)

print("-" * 60)
mySrs01 = pd.Series(x, index=['a', 'b', 'c', 'd', 'e'])
print(mySrs01)

