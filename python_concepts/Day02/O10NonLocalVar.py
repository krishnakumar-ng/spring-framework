
def outerFun():
    name = "Sachin"         # local
    def innerFun():
        nonlocal name
        name = "Mr." + name
        print("Hello World")
        print(f"Greetings {name}")

    innerFun()

outerFun()
