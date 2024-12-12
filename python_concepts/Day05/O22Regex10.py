

import re

st = "boat"
print(f"st :{st}")

res = re.match(r'b(oa|es)t', st)
# res = re.match(r'b[oe][as]t', st)

if res:
    print("Match Found.....")
    print(res.group(0))             # string that matched regex
else:
    print("Match not found.....")