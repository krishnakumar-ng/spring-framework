
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)
t2 = (1, 2, 3, 4, 5, 'six', 'seven', True, False)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 = 10,
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)
l1 = [[1, 2, 3], [4, 5, 6]]
d1 = {
    'sachin': {'test': 16500, 'odi': 18230, 't20': 1400},
    'rahul': {'test': 13200, 'od1': 15800, 't20': 1230}
}

print(f"l1 :{l1}")
print(type(l1))

print(f"d1: {d1}")
print(type(d1))

print("-" * 60)
tp1 = [1, 2, 3],
print(f"tp1 :{tp1}")
print(type(tp1))

print("-" * 60)
tp2 = {'sachin': {'test': 16500, 'odi': 18230, 't20': 1400}},
print(f"tp2 :{tp2}")
print(type(tp2))


print("-" * 60)
t4 = 1, 2, 3, 4, 5
print(f"t4 :{t4}")
print(type(t4))

print("-" * 60)
# immutable
t1 = (1, 2, 3, 4, 5)
print(f"t1 :{t1}")

print(f"t1[1] :{t1[1]}")
# t1[1] = 200

lst1 = list(t1)
print(f"lst1 :{lst1}")

lst1.extend([6, 7, 8, 9, 10])
t1 = tuple(lst1)
print(f"t1 :{t1}")

print("-" * 60)
print(dir(t1))

t1 = (1, 2, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 3, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)

# index
print(f"t1 :{t1}")

print("-" * 60)
print("first 3 :", t1.index(3))
print("second 3 :", t1.index(3, t1.index(3)+1))
print("third 3 :", t1.index(3, t1.index(3, t1.index(3) + 1) + 1))

print("-" * 60)
print(f"1's :{t1.count(1)}")
print(f"2's :{t1.count(2)}")
print(f"3's :{t1.count(3)}")

