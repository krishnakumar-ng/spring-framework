
import re

st = "our book covers both multithreaading and threading concepts"

# res = re.search(r"\bth\w+", st)
res = re.search(r"\Bth\w+", st)    # only sub strings

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")
