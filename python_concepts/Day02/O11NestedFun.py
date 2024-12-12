
def outerFun():
    gname = "Sachin"
    def innerFun():

        print(f"Greetings {gname}")
        print("Hello World")

    innerFun()

outerFun()

