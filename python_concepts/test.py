from day1 import PinLimitExceededException,Circle

class TestPin:
    @classmethod
    def verifyPin(self):
        self.limit = 3
        self.count = 0
        self.originalpin = "0000"
        self.pin = ""
        try:
            while(self.count < self.limit and self.pin != self.originalpin):
                self.pin = input("Enter your pin: ")
            
                self.count+=1
            if(self.count >= 3):
                raise PinLimitExceededException("You entered incorrect pin 3 times")
        except PinLimitExceededException as e:
            print(e)
        else:
            print("Welcome to the Application")

p = TestPin()

p.verifyPin()


c = Circle()
c.area()