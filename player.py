class Player:
    name = "Oskar"
    def __init__(self, name, HP, ATKMIN, ATKMAX, MANA):
        self.name = name
        self.HP = HP
        self.HPMAX = self.HP
        self.ATKMIN = ATKMIN
        self.ATKMAX = ATKMAX
        self.MANA = MANA
        self.MANAMAX =  self.MANA
        self.gold = 9000
        self.band = 2
        self.pot = 0
        self.draught = 0

    def __repr__(self):
        string1 = f"   {self.name}:\n   HP: {self.HP}/{self.HPMAX}\n"
        string2 = f"   ATK: {self.ATKMIN} -> {self.ATKMAX}\n   MANA: {self.MANA}/{self.MANAMAX}"
        return string1 + string2
    
    def restore_health(self, item):
        if item == "band":
            if player.band > 0:
                player.HP += 15
                player.band -= 1
                print("You used 1 bandage and restored 20HP!")
            else:
                print("You have no bandages!")

        elif item == "pot":
            if player.pot > 0:
                player.HP += 40
                player.pot -= 1
                print("You used 1 health potion and restored 40HP!")
            else:
                print("You have no health potions!")

        elif item == "draught":
            if player.draught > 0:
                player.HP += 100
                player.draught -= 1
                print("You used 1 draught of healing and restored 100HP!")
            else:
                print("You have no draughts of healing!")
        if player.HP > player.HPMAX:
            player.HP = player.HPMAX
        input("# ")
        
        



player = Player(Player.name, 100, 4, 8, 25)
    