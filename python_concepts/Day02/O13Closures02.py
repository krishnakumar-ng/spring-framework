
def outerFun(greet):

    def innerFun(name):

        print(greet, name)

    return innerFun

# Simple curry
engGrt = outerFun("Hello")
tmlGrt = outerFun("Vanakkam")

engGrt("Sachin")
tmlGrt("Ashwin")
