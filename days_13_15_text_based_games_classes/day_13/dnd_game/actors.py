import random, math


class Creature:

    def __init__(self, name: str, level: int, habitat: str):
        self.name = name
        self.level = level
        self.habitat = habitat

    def defensive_roll(self):
        roll = random.randint(1, 20)
        print(f"{self.name} rolls a {roll}...")
        attack_value = roll * self.level
        print(f"The level multiplier brings the attack value to {attack_value}")
        return attack_value


class Tiger(Creature):

    def __init__(self, name: str, level: int, habitat: str, color: str, intimidation: float):
        """Intimidation is a float which is > 1.0 for adults, and < 1.0 for cubs"""
        super().__init__(name, level, habitat)
        self.color = color
        self.intimidation = intimidation

    def defensive_roll(self):
        attack_value = super().defensive_roll()
        bonus_attack = int(math.floor(attack_value * self.intimidation))
        print(f"The {self.name} is intimidating you, improving it's attack value to {bonus_attack}")
        return bonus_attack


class RatKing(Creature):

    def __init__(self, name: str, level: int, habitat: str, number_of_underlings: int):
        """number_of_underlings is an integer. The more underlings, the stronger the king"""
        super().__init__(name, level, habitat)
        self.number_of_underlings = number_of_underlings

    def defensive_roll(self):
        attack_value = super().defensive_roll()
        bonus_attack = attack_value + (5 * self.number_of_underlings)
        print(f"The {self.name} army of rats increases his power, improving it's attack value to {bonus_attack}")
        return bonus_attack

class Wizard(Creature):

    def __init__(self, name: str, level: int, habitat=None):
        super().__init__(name, level, habitat)

    def attack(self, creature):
        my_roll = super().defensive_roll()
        creature_roll = creature.defensive_roll()
        if my_roll >= creature_roll:
            print(f"You've slain the {creature.name}!")
        else:
            print(f"You have been slain by the {creature.name}... Too bad. So sad.")
        return my_roll >= creature_roll
