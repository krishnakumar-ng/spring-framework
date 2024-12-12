
import re

st = "b7t"
print(f"st :{st}")

# res = re.match(r'b[aeiou]t', st)
# res = re.match(r'b[^aeiou]t', st)
res = re.match(r'b[a-zA-Z0-9]t', st)

if res:
    print("Match Found.....")
    print(res.group(0))             # string that matched regex
else:
    print("Match not found.....")