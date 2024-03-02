from functions import *

run = True
menu = True
info = False
play = False

# Game Loop
while run:

    while menu:
        main_menu()

        choice = input("# ")

        if choice == "1":
            clear()
            name = input("Name your character: ")
            if len(name) < 1:
                player.name = Player.name
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
        print("   0 - MAIN MENU")
        draw()
        choice = input("# ")
        if choice == "0":
            menu = True
            play = False