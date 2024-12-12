
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"player initialized {name} and age {age}")

    @staticmethod
    def get_runs():
        print(f"runs scored ..")

    def __del__(self):
        print("player deleted ... ")

sachin = Player("Sachin", 20)
Player.get_runs()