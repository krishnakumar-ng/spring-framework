
import re

st = "hello23432&34546456world"

res = re.search(r"\d+", st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")
