import random
class Enemy:
    def __init__(self, name, hp, atkmin, atkmax, gold):
        self.name = name
        self.HP = hp
        self.HPMAX = hp
        self.ATKMIN = atkmin
        self.ATKMAX = atkmax
        self.gold = gold

    def attack(self, player):
        damage = random.randint(self.ATKMIN, self.ATKMAX + 1)
        player.HP -= damage
        player.HP = max(player.HP, 0)
        print(f"{self.name} hit you for {damage} damage!")

# Enemy init
giant_rat = Enemy("Giant Rat", 20, 3, 6, 10)
drunkard = Enemy("Drunkark", 30, 4, 8, 15)
thief = Enemy("Thief", 40, 7, 14, 20)
syndicate_thug = Enemy("Syndicate Thug", 60, 10, 18, 30)