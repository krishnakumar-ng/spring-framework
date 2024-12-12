
import re

lno = "LCNO-KAR-06-2024-0001"

res = re.search(r'^LCNO-(KAR|KER|TND|APN|TLS|MAH|GOA)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-(?!0000)([0-9]{4})', lno)

"""
[0-7][1-9] - 79, multiples of 10's
([0-9]{3}[1-9]) - 1000, 2010
"""
if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found.....")
