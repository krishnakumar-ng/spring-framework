
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(name):

            from emojis import emojis
            x = emojis.encode(greet + " :" + sep + ": " + name)
            print(x)

        return innerMostFun

    return innerFun

engGrt = outerFun("Hello")
kanGrt = outerFun("Namaskara")

engGrtTgr = engGrt("bear")
kanGrtTgr = kanGrt("tiger")

engGrtTgr("Sachin")
kanGrtTgr("Prabhakar")



"""
engGrt = outerFun("Hello")
tmlGrt = outerFun("Vanakkam")

engGrtSngArw = engGrt("------>")
tmlGrtSngArw = tmlGrt("------>")

engGrtDblArw = engGrt("=====>>")
tmlGrtDblArw = tmlGrt("=====>>")


engGrtSngArw("Rohit")
tmlGrtSngArw("Ashwin")

engGrtDblArw('Virat')
tmlGrtDblArw('Srikanth')
"""