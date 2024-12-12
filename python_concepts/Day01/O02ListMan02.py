
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

print(f"l1[2] :{l1[2]}")

# insert a new value
l1[3] = 35
print(f"l1 :{l1}")

print("-" * 60)
# insert, extend, append

l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(3, 3.5)
print(f"l1 :{l1}")

print("-" * 60)
l1.append(6)
l1.append(7)
print(f"l1 :{l1}")

print("-" * 60)
l1.extend([8, 9, 10])
print(f"l1 :{l1}")
l1.extend([11])
print(f"l1 :{l1}")


print("-" * 60)
# sort, copy

l1 = [9, 7, 10, 1, 8, 3, 5, 2, 4, 6]
print(f"l1 :{l1}")

"""
l1.sort()   - sort the original list
sorted(l1)  - take a copy of the list sort it and return the sorted list
"""

res_asc = sorted(l1)
print(f"Ascending :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending :{res_desc}")


print("-" * 60)
l1 = [9, 'zebra', 7, 'yellow', 10, 'apple', 1, 'xray', 8, 'blue', 3, 'violet', 5, 'green', 2, 'white', 4, 'pink', 6, 'orange', 'queen', 'dog', 'cat', 'ultra', 'egg', 187, 1234, 26, 235, 2089 ]
print(f"l1 :{l1}")

print("-" * 60)
res_asc = sorted(l1, key=ascii)
print(f"Ascending  :{res_asc}")

for i in range(0, len(l1)):
    if type(res_asc[i]) == int:
        print(i)
        break

res = res_asc[:15] + sorted(res_asc[15:])
print(f"Ascending :{res}")

print("-" * 60)
cities  = ['thiruvananthapuram', 'hyderabad', 'mumbai', 'vishakapatnam', 'chennai', 'bangalore', 'kolkata', 'ooty', 'delhi',
           'pune']

print(f"cities :{cities}")

print("-" * 60)
cities.sort(key=len)

print(f"cities :{cities}")

print("-" * 60)
months = ['dec', 'sep', 'aug', 'nov', 'jul', 'oct', 'feb', 'may', 'jan', 'mar', 'jun', 'apr' ]

print(f"unsorted :{months}")

print("-" * 60)
# sort these months according to the calendar
from calendar import month_abbr
print(list(month_abbr))

print("-" * 60)
res = sorted(months, key=list(map(lambda mth: mth.lower(), list(month_abbr))).index)
print(f"res :{res}")
