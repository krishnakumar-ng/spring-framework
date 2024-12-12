
import re

st = "the quick brown fox jumps over the lazy dog."

print(f"st :{st}")

res = re.sub(r't\w+', "The", st, 1)
print(f"res :{res}")

print("-" * 60)
print(st.replace("the", "The", 1))
