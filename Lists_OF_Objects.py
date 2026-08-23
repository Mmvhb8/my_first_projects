# 1. Define a class
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def heal(self, amount):
        self.health = self.health + amount   # change state
# 2. Create objects
warrior = Hero("Thorin", 100)
mage = Hero("Lyra", 70)
rogue = Hero("Shade", 80)
# 3. Put them in a list
party = [warrior, mage, rogue]
# 4. Loop: read + act
for hero in party:
    print(hero.name, hero.health)  # read data
    hero.heal(10)                  # trigger behavior (side effect)
# 5. Check results after loop
print("After healing:")
for hero in party:
    print(hero.name, hero.health)