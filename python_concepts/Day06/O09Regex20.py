"""
there are three parts in the string
1. the string that did'nt match the regex  - the quick brown
2. the string that match regex - fox
3. the string that is yet to be checked - jumps over the lazy dog
"""

import re

st = "the quick brown fox jumps over the lazy dog"

res = re.search(r'(f\w+)', st)

if res:
    print("Match found.....")
    print("-" * 60)
    print("String Rejected -", st[:res.start()])
    print("-" * 60)
    print("String Matched -", res.group(0))
    print("-" * 60)
    print("Sting Unchecked -", st[res.end():])
else:
    print("Match not found.....")
