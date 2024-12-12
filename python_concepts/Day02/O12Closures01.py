
def outerFun():
    gname = "Sachin"

    def innerFun():

        print(f"Greetings {gname}")
        print("Hello World")

    return innerFun

outerFun()()            # calls the innerFun

print("-" * 60)
inref = outerFun()
print("After few lines of code.....")

inref()
