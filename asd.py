import json
import random

with open("kaland.json", "r", encoding="utf-8") as f:
    data = json.load(f)

class Character:
    def __init__(self, name, skill, health, damage):
        self.name = name
        self.skill = int(skill)
        self.health = health
        self.damage = damage

    def generate_skill(self):
        self.skill = random.randint(1, 100)


a = Character("jatekos",1 ,1,1 )

print(a.generate_skill())
print(a.skill)