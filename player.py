class Player:
    name = "Oskar"
    def __init__(self, name, HP, ATKMIN, ATKMAX, armor, MANA):
        self.name = name
        self.HP = HP
        self.HPMAX = self.HP
        self.ATKMIN = ATKMIN
        self.ATKMAX = ATKMAX
        self. armor = armor
        self.MANA = MANA
        self.MANAMAX =  self.MANA

    def __repr__(self):
        string1 = f"   {self.name}:\n   HP: {self.HP}/{self.HPMAX}\n"
        string2 = f"   ATK: {self.ATKMIN} -> {self.ATKMAX}\n   ARMOR: {self.armor}\n   MANA: {self.MANA}/{self.MANAMAX}"
        return string1 + string2
player = Player(Player.name, 100, 4, 8, 20, 25)