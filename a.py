import json
import random

# Betöltjük az enemy és a player adatait a JSON fájlból
with open('kaland.json', 'r') as f:
    enemy_data = json.load(f)

with open('kaland.json', 'r') as f:
    player_data = json.load(f)

# Meghatározzuk a kezdő életerőket
enemy_health = enemy_data['health']
player_health = player_data['health']

# Harc loop
while enemy_health > 0 and player_health > 0:
    # Az enemy dob egy dobókockát az attack értékével megszorozva
    enemy_damage = random.randint(1, 6) * enemy_data['attack']

    # A player dob egy dobókockát a defense értékével csökkentve
    player_defense = player_data['defense']
    player_damage = random.randint(1, 6) - player_defense
    if player_damage < 0:
        player_damage = 0

    # Csökkentjük az életerőt a kapott sebzések alapján
    enemy_health -= player_damage
    player_health -= enemy_damage

    # Kiírjuk a kapott sebzéseket és az aktuális életerőket
    print("Player sebzése: " + str(enemy_damage))
    print("Enemy sebzése: " + str(player_damage))
    print("Player életerő: " + str(player_health))
    print("Enemy életerő: " + str(enemy_health))

# Kiírjuk az eredményt
if enemy_health <= 0:
    print("A player nyert!")
else:
    print("Az enemy nyert!")