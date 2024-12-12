
import re

st = "baaaaaaaaaaaaaaaaaaaaaaaaaat"
print(f"st :{st}")

# * is applicable only for a
res = re.match(r'ba*t', st)

if res:
    print("Match Found.....")
    print(res.group(0))             # string that matched regex
else:
    print("Match not found.....")