"""A component for the Entity class. Components are an alternative to inheritance.
Essentially, if an Entity can fight, it will take on this fighter component. If it can't, it won't.
"""
import libtcodpy as libtcod
from game_messages import Message


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
                {'message': Message("{} attacks {} for {} damage!".format(
                    self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)}
            )
            results.extend(target.fighter.take_damage(damage))  # Extend keeps the list one-dimensional
        else:
            results.append(
                {'message': Message("{} attacks {}, but it's laughed off!".format(
                    self.owner.name.capitalize(), target.name), libtcod.white)}
            )

        return results

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner})

        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp
