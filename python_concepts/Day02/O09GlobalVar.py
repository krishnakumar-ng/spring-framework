
glbX = 100

def fun(x):
    global glbX             # do not assign any values in this line
    print(f"x :{x}")
    glbX = 10
    print(f"glbx :{glbX}")


print(f"Before :{glbX}")

fun(10)

print(f"After :{glbX}")
