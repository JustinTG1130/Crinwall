from functions import *

def shop():
    shop = True
    while shop:
        clear()
        draw()
        print(player)
        draw_long()
        print("  1 - |30GP| UPGRADE WEAPON (+2/+5 min/max)")
        print("  2 - |25GP| UPGRADE HEALTH (+10 max hp)")
        print("  3 - |10GP| BANDAGES (+15HP)")
        print("  4 - |25GP| HEALTH POTION (+40HP)")
        print("  5 - |55GP| DRAUGHT OF HEALING (+100HP)")
        print("  0 - LEAVE")
        draw_long()

        choice = input("# ")

        # Upgrade damage
        if choice == "1":
            if player.gold >= 30:
                if player.ATKMAX < 58:
                    player.gold -= 30
                    player.ATKMIN += 2
                    player.ATKMAX += 5
                    print(f"Your minimum attack increased by 2, and your maximum by 5!")
                    print(f"ATK: {player.ATKMIN-2} -> {player.ATKMIN} / {player.ATKMAX-5} -> {player.ATKMAX}")
                
                else:
                    print("You cannot upgrade your weapon any further!")
    
            else:
                print("You don't have enough gold!")
            input("# ")
        
        # Upgrade max hp
        elif choice == "2":
            if player.gold >= 25:
                if player.HPMAX <= 200:
                    player.gold -= 25
                    player.HPMAX += 10

                    print("Your maximum hp increased by 10")
                    print(f"HP: {player.HP} / {player.HPMAX - 10} -> {player.HPMAX}")
                else:
                    print("You cannot upgrade your hp any further")
            else:
                print("You don't have enough gold!")
            input("# ")
        
        # Bandages
        elif choice == "3":
            if player.gold >= 10:
                player.gold -= 10
                player.band += 1
                print("You bought 1 bandage")
            else:
                print("You don't have enough gold!")
            input("# ")

        # Potion of healing
        elif choice == "4":
            if player.gold >= 25:
                player.gold -= 25
                player.pot += 1
                print("You bought 1 health potion")
            else:
                print("You don't have enough gold!")
            input("# ")

        # Draught of healing
        elif choice == "5":
            if player.gold >= 55:
                player.gold -= 55
                player.draught += 1
                print("You bought 1 draught of healing")
            else:
                print("You don't have enough gold!")
            input("# ")

        elif choice == "0":
            shop = False
        