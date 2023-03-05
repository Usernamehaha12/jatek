import random
import json

with open("kaland.json", "r", encoding="utf-8") as f:
    data = json.load(f)


class Character:
    def __init__(self, name, skill=6, health=12, damage=0, luck=6):
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
        self.damage = self.luck + random.randint(1, 12)


a = Character("jatekos")

a.generate_skill()
a.generate_health()
a.generate_luck()
a.generate_damage()

lepes = 1
k = 0
szoveg = data["kartyak"][k]["szoveg"]
akcio = data["kartyak"][k]["akcio"]




enter = input("Sorsold ki a képeségeidet(enter)")
if a.health != 0:
    if enter == "":
        print(f"Életerőd:{a.health}")
        print(f"Ügyességed:{a.skill}")
        print(f"Szerencséd:{a.luck}")
        print(f"Sebzésed:{a.damage}")
    else:
        print("nem ez enter nyomtad meg.")


    enter1 = input("Kezd el a játékot (enter)")
    if a.health != 0:
        if enter1 == "":
            print(data["bevezeto"])
        else:
            print("nem ez enter nyomtad meg.")
while a.health != 0:

        enter2 = input(f"Lapozz {lepes} (enter)")
        if akcio["tipus"] == "ugrás":
            lepes = (data["kartyak"][k]["akcio"]["ugras"])
            k = (data["kartyak"][k]["akcio"]["ugras"][0])
            szoveg = data["kartyak"][k]["szoveg"]

            print(szoveg, k)

        elif akcio["tipus"] == "harc":
            lepes = (data["kartyak"][k]["akcio"]["ugras"])
            k = (data["kartyak"][k][["ugras"][-1]])
            szoveg = data["kartyak"][k]["szoveg"]

            print("valami")

        elif akcio["tipus"] == "választás":
            lepes = (data["kartyak"][k]["akcio"]["ugras"])
            k = (data["kartyak"][k]["ugras"])
            szoveg = data["kartyak"][k]["szoveg"]

            print("valami")

        elif akcio["tipus"] == "ügyességpróba":
            k1 = (data["kartyak"][k]["akcio"]["ugras"[1]])
            print("proba")








