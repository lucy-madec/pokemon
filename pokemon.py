class Pokemon:
    def __init__(self, name, type, hp, level, attack_power, defense):
        self.name = name
        self.type = type
        self.hp = hp
        self.level = level
        self.attack_power = attack_power
        self.defense = defense

    def display_pokemon(self):
        