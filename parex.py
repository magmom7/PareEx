class monster:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def attack(self):
        print(self.skill, "을 수행합니다.")


class person(monster):
    def __init__(self, name, skill, health):
        self.name = name
        self.skill = skill
        self.health = health
