from functions import *
from shop import *

run = True
menu = True
info = False
play = False

# MAP 
        #     x = 0       x = 1       x = 2       x = 3      x = 4
map = [["warehouse",           "street",    "house",   "temple",   "house"],    # y = 0
        [    "house",          "street", "townhall",   "street",  "jewler"],    # y = 1
        [    "house",          "street",    "tower",   "street",   "house"],    # y = 2
        [      "inn",          "street",   "street",   "street",   "house"],    # y = 3
        [     "shop",   "town entrance",   "stables",   "house",   "house"]]    # y = 4
    
y_len = len(map) -1
x_len = len(map[0]) -1

# Tile info
# First key gets the tile from the map
# "t" key: designates offical name
# "e" key: True means an enemy can spawn on that tile
tile ={
    "town entrance": {
        "t": "TOWN GATE",
        "e": True},
    "house": {
        "t": "HOUSE",
        "e": True},
    "street": {
        "t": "STREET",
        "e": True},
    "inn": {
        "t": "INN",
        "e": False},
    "tower": {
        "t": "TOWER",
        "e": False},
    "townhall": {
        "t": "TOWNHALL",
        "e": False},
    "temple": {
        "t": "TEMPLE OF NILLAMOR",
        "e": False},
    "jewler": {
        "t": "JEWLER",
        "e": False},
    "stables": {
        "t": "STABLES",
        "e": True},
    "warehouse": {
        "t": "WAREHOUSE",
        "e": True},
    "shop": {
        "t": "SHOP",
        "e": False}}

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

        print("   LOCATION: " + tile[map[player.y][player.x]]["t"])

        draw()

        print(player)

        draw()

        # Tells player what direction they can move
        print("   MOVEMENT")
        print(f"   COORDS X: {player.x} | Y: {player.y}")
        # Checks to see if player is at the edge of the map, and if so, it gives them the option to move.
        if player.y > 0: 
            print("   w - NORTH")
        if player.x > 0:
            print("   a - WEST")
        if player.y < y_len:
            print("   s - SOUTH")
        if player.x < x_len:
            print("   d - EAST")

        draw()

        # Number options
        print("   5 - SHOP")
        print("   8 - INVENTORY")
        print("   9 - SAVE GAME")
        print("   0 - MAIN MENU")

        draw()
        dest = input("# ")

        if dest == "w":
            if player.y > 0:
                player.y -= 1
        
        elif dest == "a":
            if player.x > 0:
                player.x -= 1

        elif dest == "s":
            if player.y < y_len:
                player.y += 1

        elif dest == "d":
            if player.x < x_len:
                player.x += 1
        
        # Logic for destinations
        elif dest == "5":
            shop()

        elif dest == "8":
            inventory()

        elif dest == "0":
            menu = True
            play = False