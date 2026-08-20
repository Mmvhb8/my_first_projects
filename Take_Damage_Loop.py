class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount

heroes = [
    Hero("Warrior", 100),
    Hero("Mage", 50),
    Hero("Cleric", 80),
]

print("Before turn:")
for h in heroes:
    print(h.name, "HP:", h.health)

total_damage = 0
badly_hurt_count = 0

for hero in heroes:
    hero.take_damage(10)
    total_damage += 10
    if hero.health < 50:
        badly_hurt_count += 1

print("After turn:")
for h in heroes:
    print(h.name, "HP:", h.health)

print(f"Party took: {total_damage} damage")
print("Badly hurt heroes:", badly_hurt_count)