
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 60)
s2 = {1, 2, 3, 4, 'five', 'six', 'seven', 'eight', 'nine', 10+3j, 11-1j, 12.0, 13.5, 14.2, True, False}
print(f"s2 :{s2}")
print(type(s2))

# add, update, remove, pop, discard
print("-" * 60)
s1 = set()
print(f"s1 :{s1}")

# add
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(1)
s1.add(2)
s1.add(4)
s1.add(3)

print(f"s1 :{s1}")
print("-" * 60)

# update
s1.update([1, 2, 3])
s1.update([3, 4, 5])
s1.update([2, 3, 4])
s1.update([6, 7, 8])
s1.update([5, 6, 7])
s1.update([7, 9, 10])

print(f"s1 :{s1}")

print("-" * 60)
# pop
res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")

print("-" * 60)
# remove
s1.remove(8)
s1.remove(10)

# s1.remove(1)
print(f"s1 :{s1}")

print("-" * 60)
# discard
s1.discard(4)
s1.discard(6)

s1.discard(1)
print(f"s1 :{s1}")

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 60)
print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print(f"A symmetric_difference B :{A ^ B}")
print(F"B symmetric_difference A :{B.symmetric_difference(A)}")

print("-" * 60)
# frozenset = immutable
f1 = frozenset([1, 2, 3, 4, 5])
print(f"f1 :{f1}")
print(type(f1))
