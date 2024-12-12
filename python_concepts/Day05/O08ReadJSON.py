
import json

FL = open("books.json", "r")
jsonFR = json.load(FL)

# print(jsonFR)

for book in jsonFR['books']:
    print(book['name'])
    print("-" * len(book['name']))
    print([{k: v} for k, v in book.items() if k != "name"])

    print("-" * 60)

print("-" * 60)
# data is enclosed in single quotes
empdata = '{"name": "Mike", "age": 32, "desig": "MGR", "dept": "MKT"}'
print(f"empdata :{empdata}")
print(type(empdata))

print("-" * 60)
res = json.loads(empdata)
print(f"res: {res}")
print(type(res))



"""
json.load - takes the file object and returns the json object. It is used to read JSON encoded data from a file and convert it into python dictionary and deserialize the file (accept the file object) 

------------------------------------------------------------------------------
json.loads() - method can be ised to parse a valid JSON string and convert it into a Python Dictionary. It is mainly used for deserializing native string, byte or byte array which consists of JSON data into python Dictionary

"""