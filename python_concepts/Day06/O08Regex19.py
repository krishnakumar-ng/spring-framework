
import re
# back tracking

st = "good blood bad blood"
# \2 - recall the second grouping - data also should match

res = re.search(r"(\w+)\s(\w+)\s(\w+)\s(\2)", st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found....")