class Wizard:
    def __init__(self, name, mana):
        self.name = name
        self.mana = mana
    def spend_mana(self, amount):
        self.mana -= amount
    def cast_fireball(self, target, mana_cost, damage):
        self.spend_mana(mana_cost)
        target.take_damage(damage)

class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def take_damage(self, amount):
        self.hp -= amount

wizard = Wizard("Bryan", 15)
monster = Monster("Goblin", 30)

wizard.cast_fireball(monster, 5, 15)
print(wizard.name, "Mana", wizard.mana, monster.name, "hp", monster.hp)