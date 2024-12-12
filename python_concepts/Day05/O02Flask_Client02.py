
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getproduct/pepsi")

res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
