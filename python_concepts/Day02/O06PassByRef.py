
def fun(names):
    print(f"inside :{names}")
    # team = names.copy()
    # team.extend(["Joel", "Mary", "Kenith"])
    names.extend(["Joel", "Mary", "Kenith"])
    print(f"after modification :{names}")

lst1 = ['John', 'Kevin', 'Richard', 'Peter', 'Harry']
print(f"before :{lst1}")
fun(lst1)

print(f"after call :{lst1}")
