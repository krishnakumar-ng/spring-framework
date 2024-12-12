
import re

st = "The quick brown fox jumps over the lazy dog"

# res = re.search(r"\Athe", st, re.I)
# res = re.search(r'[a-z]+', st, re.I)
res = re.search(r"dog\Z", st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")

print("-" * 60)
print(dir(re))

