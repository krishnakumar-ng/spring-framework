
fruits = [
    ('apple', 285),
    ('orange', 65),
    ('grapes', 180),
    ('banana', 75),
    ('gauva', 120),
    ('pine apple', 150),
    ('pears', 220),
    ('strawberry', 350)
]

print(f"fruits :{fruits}")
print("-" * 60)

price = ["fruits" for fruit in fruits]
print(f"price :{price}")

print("-" * 60)
price = [fruit for fruit in fruits]
print(f"price :{price}")

print("-" * 60)
price = [fruit[0] for fruit in fruits]
print(f"price :{price}")

print("-" * 60)
price = [fruit[1] for fruit in fruits]
print(f"price :{price}")

print("-" * 60)
price = [fruit[1] for fruit in fruits]
print(f"price :{price}")

print("-" * 60)
price = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75]
         for fruit in fruits]
print(f"price :{price}")


print("-" * 60)
price = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75]
         for fruit in fruits if fruit[1] > 100]
print(f"price :{price}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

words = [word for word in sentence.split()]
print(f"words :{words}")

print("-" * 60)
words = [word for word in sentence.split() if word != 'the']
print(f"words :{words}")

print("-" * 60)
words = [word for word in sentence.split() if len(word) > 3]
print(f"words :{words}")




