
import re

st = "sample.py"
print(f"st :{st}")

# . is a single regex
res = re.search(r'\.py$', st)

if res:
    print("Match Found.....")
    print(res.group(0))             # string that matched regex
else:
    print("Match not found.....")