
l1 = list()
print(f"l1 :{l1}")   # interpolation
print(type(l1))      # RTTI - Run Time Type Identification

print("-" * 60)
l2 = [1, 2, 3, 4, 5.0, 6.3, 7.8, 8.25, 9+2j, 10-3j, 'eleven', 'twelve', 'thirteen', 'fourteen', True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
l1 = [1, 2, 3, 4, 5]
print("l1 :", l1)
# unpack
print("l1 :", *l1)

print("-" * 60)
values = list(range(10, 31, 10))
print(f"values :{values}")
x = values
print(f"x :{x}")
print(type(x))

# unpacking
a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values
print(a, b, c, sep=", ")
print("-" * 60)

a, *b, c = values
print(a, b, c, sep=", ")
print("-" * 60)

*a, b, c = values
print(a, b, c, sep=", ")
print("-" * 60)

print("-" * 60)
lst1  = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

lst3 = [lst1, lst2]
print(len(lst3))
print(f"lst3 :{lst3}")

lst4 = [*lst1, *lst2]       # unpack
print(len(lst4))
print(f"lst4 :{lst4}")

print("-" * 60)
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

print("-" * 60)
for letter in letters:
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0], "\t",  letter[1])

print("-" * 60)
for index, letter in enumerate(letters):
    print(f"{index}\t{letter}")

print("-" * 60)
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(mylist)

print("-" * 60)
for lst in mylist:
    print(lst)

print("-" * 60)
for index, lst in enumerate(mylist):
    print(f"{index}\t{lst}")

print("-" * 60)
for index, lst in enumerate(mylist):
    print(f"List({index})")
    for ind, l in enumerate(lst):
        print(f"\t{ind}\t{l}")
