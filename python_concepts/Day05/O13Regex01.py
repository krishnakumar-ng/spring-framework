
import re

st = "hello world"
print(f"st :{st}")

res = re.match(r'^hello', st)
print(res)

if res:
    print("Match Found.....")
    print(res.group(0))             # string that matched regex
else:
    print("Match not found.....")