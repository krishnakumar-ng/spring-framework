class Team:
    headname = "Virat"

    def __init__(self, name):
        self.t_name = name

    @classmethod
    def print_headname(cls):
        print(f"headname = {cls.headname}")

    @classmethod
    def set_headname(cls, name):
        cls.headname = name


india = Team("india")

Team.set_headname("Dhoni")
Team.print_headname()