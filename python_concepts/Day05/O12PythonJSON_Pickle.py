
"""
Json Module

a. using json module we can serialize and deserialize several python types like bool, int, string, float, dict, list, tuple etc...

b. it is very good choice for interoperability among different languages
"""
import json
data = {"name": "Sachin", "age": 36, "oppn": "Aus", "venue": "Perth"}
json_obj = json.dumps(data)

print(json_obj)
print("serialization completed")
print(type(json_obj))

print("-" * 60)
# convert it back to python dictionary
player = json.loads(json_obj)
print(player)
print("Deserialization completed.....")
print(type(player))
