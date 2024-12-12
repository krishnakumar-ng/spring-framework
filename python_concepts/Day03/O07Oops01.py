
class Player:

    def get_runs(self):
        print("Runs Scored......")
        print(self.__class__)

sachin = Player()
sachin.get_runs()

print(type(sachin))
print(sachin.__class__)

print("-" * 60)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))

