import random
class Player:
    name = "Oskar"
    def __init__(self, name, HP, ATKMIN, ATKMAX, MANA):
        # Stats
        self.name = name
        self.HP = HP
        self.HPMAX = self.HP
        self.ATKMIN = ATKMIN
        self.ATKMAX = ATKMAX
        self.MANA = MANA
        self.MANAMAX = self.MANA

        # Inventory
        self.gold = 0
        self.band = 2
        self.pot = 0
        self.draught = 0

        #Coords
        self.x = 1
        self.y = 4
        self.idle = True

    # Shows player name and stats
    def __repr__(self):
        string1 = f"   {self.name}:\n   HP: {self.HP}/{self.HPMAX}\n"
        string2 = f"   ATK: {self.ATKMIN} -> {self.ATKMAX}\n   MANA: {self.MANA}/{self.MANAMAX} \n   GOLD: {self.gold}"
        return string1 + string2
    
    # Restore health
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
    
    # Player Attack
    def attack(self, target):
        damage = random.randint(self.ATKMIN, self.ATKMAX + 1)
        target.HP -= damage
        target.HP = max(target.HP, 0)
        print(f"You dealt {damage} damage to {target.name}!")

        
# player init
player = Player(Player.name, 100, 4, 8, 25)
    