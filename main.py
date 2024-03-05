from functions import *
from shop import *

run = True
menu = True
info = False
play = False

# Game Loop
while run:

    while menu:
        clear()
        main_menu()

        choice = input("# ")

        if choice == "1":
            clear()
            name = input("Name your character: ")
            if len(name) < 1:
                player.name = Player.name
            else:
                player.name = name
            menu = False
            play = True
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            quit()
        

    while play:
        clear()
        draw()
        print(player)
        draw()
        print("   5 - SHOP")
        print("   8 - INVENTORY")
        print("   9 - SAVE GAME")
        print("   0 - MAIN MENU")
        draw()
        choice = input("# ")
        if choice == "5":
            shop()
        elif choice == "8":
            inventory()
        elif choice == "0":
            menu = True
            play = False