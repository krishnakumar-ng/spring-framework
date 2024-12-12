
import re

st = """
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
"""
# match is a variable
for match in re.finditer(r't\w+', st):
    # print(match)
    s = match.start()
    e = match.end()
    print(f"Match found between {s} and {e} :{st[s:e]}")