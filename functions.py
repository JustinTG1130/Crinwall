import os, random
from player import *
from enemies import *
def draw():
    print("<X>--------------------<X>")
def draw_long():
    print("<X>----------------------------------------<X>")
def clear():
    os.system("cls")

def main_menu():
    clear
    draw()
    print(" | 1 - NEW GAME         |")
    print(" | 2 - LOAD GAME        |")
    print(" | 3 - INFO             |")
    print(" | 4 - QUIT GAME        |")
    draw()
def inventory():
        inventory = True
        while inventory:
            clear()
            draw()
            print("   INVENTORY: ")
            draw()
            if player.band > 0:
                print(f"   1 - BANDAGES: {player.band}")
            if player.pot > 0:
                print(f"   2 - POTION: {player.pot}")
            if player.draught > 0:
                print(f"   3 - DRAUGHT: {player.draught}")
            print("   0 - BACK")
            draw()
            choice = input("# ")
            if choice == "1":
                player.restore_health("band")
            elif choice == "2":
                player.restore_health("pot")
            elif choice == "3":
                player.restore_health("draught")
            elif choice == "0":
                inventory = False

def fight():
    fight = True
    e_list = [giant_rat, drunkard, thief, syndicate_thug]
    
    enemy = random.choice(e_list)

    while fight:

        # Combatants information
        clear()
        draw()
        print(f"   Defeat the {enemy.name}!")
        draw()
        print(f"   {enemy.name}'s HP: {enemy.HP}/{enemy.HPMAX}")
        print(f"   {player.name}'s HP: {player.HP}/{player.HPMAX}")
        print(f"   BANDAGES: {player.band}")
        print(f"   POTIONS: {player.pot}")
        print(f"   DRAUGHTS: {player.draught}")
        draw_long()

        # Actions
        print("   1 - ATTACK")
        if player.band > 0:
            print("   2 - USE BANDAGE")
        if player.pot > 0:
            print("   3 - USE POTION")
        if player.draught > 0:
            print("   4 - USE DRAUGHT")
        print("   5 - FLEE (30% CHANCE TO BE HIT)")
        draw_long()

        action = input("# ")
        if action == "1":
            player.attack(enemy)
            enemy.attack(player)
            input("# ")

        elif action == "2":
            player.restore_health("band")
            enemy.attack(player)

        elif action == "3":
            player.restore_health("pot")
            enemy.attack(player)

        elif action == "4":
            player.restore_health("draught")
            enemy.attack(player)

        elif action == "5":
            if random.randint(1, 100) < 30:
                enemy.attack(player)
            else:
                print("You got away safely!")
            fight = False

        if enemy.HP == 0:
            fight = False
            player.gold += enemy.gold
            print(f"You defeated the {enemy.name}!")
            print(f"{enemy.gold} gold was found on the {enemy.name}")
            input("# ")
        if player.HP == 0:
            print(f"You were defeated by {enemy.name}...")
            input("# ")
            clear()
            print("GAME OVER")
            input("Press enter to exit...")
            quit()