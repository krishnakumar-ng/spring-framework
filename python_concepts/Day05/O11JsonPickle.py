
"""
Pickle Module

a. it serializes python object into binary format
b. it is faster and also works with customized objects
c. better choice for serialization and deserailization of python objects
"""

import pickle

data = {"name": "Sachin", "age": 36, "oppn": "Aus", "venue": "Perth"}
print(f"data :{data}")
with open("data.pickle", "wb") as FW:
    pickle.dump(data, FW)
    print("Completed picking......")

with open("data.pickle", "rb") as FL:
    print("Unpickling the data :")
    player = pickle.load(FL)
    print(player)
