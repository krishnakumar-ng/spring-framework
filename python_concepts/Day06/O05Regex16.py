
import re

st = "hello3234234@#$%^&*     world"

# res = re.search(r"\s+", st)
res = re.search(r"\S+", st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")
