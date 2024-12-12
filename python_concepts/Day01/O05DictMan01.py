
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'sachin', 'age': 32, 'runs': 134, 'oppn': 'Aus'}
print(f"d2 :{d2}")
print(type(dict))

print("-" * 60)
d3 = dict([('name', 'Rahul'), ('age', 29), ('runs', 80), ('oppn', 'WI')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name='sourav', age=30, runs=120, oppn='PAK')
print(f'd4 :{d4}')
print(type(d4))

print("-" * 60)
player = {'name': 'sachin', 'age': 34, 'runs': 98, 'oppn': 'nzl'}
print(f"player :{player}")

print("-" * 60)
print(f"Name :{player['name']}")

print("-" * 60)
for x in player:            # referring the keys
    print(x, "=>", player[x])

print("-" * 60)
# add new key value
player['venue'] = 'auckland'
player['year'] = 2003

print(f"player :{player}")

print("-" * 60)
# modify the values
player['name'] = "Tendulkar"
player['runs'] = 85

print(f"player :{player}")

print("-" * 60)
# del

del player['age']
del player['oppn']

print(f"player :{player}")

print("-" * 60)
# print(dir(player))

k = player.keys()
v = player.values()

print(f"keys   :{k}")
print(f"values :{v}")

print("-" * 60)
for k, v in player.items():
    print(k + " => " + str(v))

print("-" * 60)
# list to a dictionary
cities = ['blr', 'che', 'hyd', 'mum', 'del', 'kol']
print(f"cities :{cities}")

print("-" * 60)
res = dict.fromkeys(cities)
print(f"res :{res}")

res = dict.fromkeys(cities, 20)
print(f"res :{res}")

print("-" * 60)
# setdefault - allows only to add new key values into the dictionary

emp = {'empid': 1030, 'empname': 'Richard', 'age': 34, 'desig': 'MGR'}
print(f"emp :{emp}")

emp.setdefault('age', 28)
emp.setdefault('desig', 'BDM')
emp.setdefault("dept", "Finance")
emp.setdefault("Loc", 'Chennai')

print(f"emp :{emp}")

print("-" * 60)

emp = {'empid': 1030, 'empname': 'Richard', 'age': 34, 'desig': 'MGR'}
print(f"emp :{emp}")

# pop, popitem

res = emp.pop("age")
print(f"res :{res}")

res = emp.pop("empname")
print(f"res :{res}")

print(f"emp: {emp}")

print("-" * 60)

emp = {'empid': 1030, 'empname': 'Richard', 'age': 34, 'desig': 'MGR'}
print(f"emp :{emp}")

res = emp.popitem()
print(f"res :{res}")

res = emp.popitem()
print(f"res :{res}")

print(f"emp :{emp}")

print("-" * 60)
# clear

emp = {'empid': 1030, 'empname': 'Richard', 'age': 34, 'desig': 'MGR'}
print(f"emp :{emp}")

emp.clear()
print(emp)

print("-" * 60)

emp = {'empid': 1030, 'empname': 'Richard', 'age': 34, 'desig': 'MGR'}
print(f"emp :{emp}")

emp['loc'] = 'hyd'
emp['sal'] = 125000

print(f"emp :{emp}")

# emp = {'eid': 2423, 'ename': 'Peter'}
# print(f"emp :{emp}")