import json
import random

class Character:
    def __init__(self,name, skill = 6, health = 12,damage = 0 , luck = 6):
        self.name = name
        self.skill = int(skill)
        self.health = int(health)
        self.damage = damage
        self.luck = luck

    def generate_skill(self):
        self.skill += random.randint(1, 6)

    def generate_health(self):
        self.health += random.randint(1, 6)

    def generate_luck(self):
        self.luck += random.randint(1, 6)

    def generate_damage(self):
        self.damage = self.luck + random.randint(1, 6)


a = Character("jatekos")

a.generate_skill()
a.generate_health()
a.generate_luck()
a.generate_damage()
print(a.skill, a.health, a.luck, a.damage)