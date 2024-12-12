
import marshal

data = {"name": "Sachin", "runs": 130, 'oppn': 'Aus', 'venue': 'Gabba'}
print(f"data :{data}")

# dumps - return byte object stored in variable 'bytes'

bytes = marshal.dumps(data)
print("After Serialization :", bytes)

print("-" * 60)
# loads() - converts byte objects into values
new_data = marshal.loads(bytes)
print("After Deserialization", new_data)
