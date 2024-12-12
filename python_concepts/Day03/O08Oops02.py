
class Player:           # Pascal casing

    def __init__(self):         # constructor
        print("Player Initialized......")

    def get_runs(self):
        print(f"Runs Scored.....")

    def __del__(self):
        print("Player deleted.....")

sachin = Player()
sourav = Player()

print("-" * 60)
sachin.get_runs()
sourav.get_runs()

print("-" * 60)
del sachin

print("-" * 60)
# sachin.__init__()



