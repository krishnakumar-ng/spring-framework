import json

import requests

BASE = "http://127.0.0.1:5000/"

print("GET".center(60, "-"))

response = requests.get(BASE + "getproduct/pepsi")

res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("put".center(60, "-"))

response = requests.put(BASE + "getproduct/coke", data={'cat': 'baverage'})

res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("PATCH".center(60, "-"))
data = {'price': 5000}

response = requests.patch(BASE + "getproduct/coke", json = json.dumps(data))
res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("POST".center(60, "-"))
fanta = {'item': '1 litre Bottle', 'price': 70, 'qty': 225}

response = requests.post(BASE + "getproduct/fanta", json = json.dumps(fanta))
res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print()

print("DELETE".center(60, "-"))
response = requests.delete(BASE + "getproduct/thumbs_up")
res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print()
