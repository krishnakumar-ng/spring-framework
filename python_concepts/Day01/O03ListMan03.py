# copy

l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy the list l1 to l2

l2 = l1         # shallow copy - copies the address with the data

print(f'l2 before :{l2}')

l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
print("=" * 60)

l3 = [10, 20, 30, 40, 50]
print(f"l3 before :{l3}")

# copy the list l3 to l4

l4 = l3.copy()          # deep copy - only data gets copied

print(f"l4 before :{l4}")

l4.insert(1, 15)
l4.insert(3, 25)
l4.insert(5, 35)
l4.insert(7, 45)

print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)
print("=" * 60)

l5 = [2, 4, 6, [5, 10, 15, 20, 25], 8, 10]
print(f"l5 before :{l5}")

# copy the l5 to l6
l6 = l5.copy()

print(f"l6 before :{l6}")
l6[3].append(30)
l6[3].append(35)
l6[3].append(40)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)
print("=" * 60)

l7 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 5]
print(f"l7 before :{l7}")

# copy the list l7 to l8
from copy import deepcopy
l8 = deepcopy(l7)

print(f"l8 before :{l8}")

l8[4].insert(1, 15)
l8[4].insert(3, 25)
l8[4].insert(5, 35)
l8[4].insert(7, 15)

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

