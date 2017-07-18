"""A component for the Entity class. Components are an alternative to inheritance.
Essentially, if an Entity can fight, it will take on this fighter component. If it can't, it won't.
"""


class Fighter:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def attack(self, target):
        results = []

        damage = self.power - target.fighter.defense

        if damage > 0:
            results.append(
                {'message': "{} attacks {} for {} damage!".format(self.owner.name.capitalize(), target.name, str(damage))}
            )
            results.extend(target.fighter.take_damage(damage))  # Extend keeps the list one-dimensional
        else:
            results.append(
                {'message': "{} attacks {}, but it's laughed off!".format(self.owner.name.capitalize(), target.name)}
            )

        return results

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner})

        return results
