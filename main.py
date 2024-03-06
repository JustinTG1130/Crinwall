from functions import *
from shop import *
import random

run = True
menu = True
info = False
play = False
time = "AM"
clock = 6

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
        "t": "TEMPLE",
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

        # Battle Checker
        if not player.idle:
            if tile[map[player.y][player.x]]["e"]:
                if clock < 18: # Less of a chance to encounter an enemy before 6pm
                    if random.randint(1,100) <= 50: # default 15
                        fight()
                if clock >= 18: # Much higher of a chance to encounter an enemy after 6pm
                    if random.randint(1,100) <= 50: # default 35
                        fight()

        draw()
        print(f"   TIME: {clock}{time}")
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
        print("   1 - INVENTORY")
        if map[player.y][player.x] == "shop" or map[player.y][player.x] == "townhall" or map[player.y][player.x] == "tower" or map[player.y] [player.x] == "temple" or map[player.y][player.x] == "inn" or map[player.y][player.x] == "jewler" or map[player.y][player.x] == "warehouse":
            print("   2 - ENTER")
        print("   9 - SAVE GAME")
        print("   0 - MAIN MENU")

        draw()
        dest = input("# ")

        # Logic for movement
        if dest == "w":
            if player.y > 0:
                player.y -= 1
                player.idle = False
        
        elif dest == "a":
            if player.x > 0:
                player.x -= 1
                player.idle = False

        elif dest == "s":
            if player.y < y_len:
                player.y += 1
                player.idle = False

        elif dest == "d":
            if player.x < x_len:
                player.x += 1
                player.idle = False
        
        # Logic for destinations
        elif dest == "1":
            inventory()
        elif dest == "2":
            if map[player.y][player.x] == "shop":
                shop()
        elif dest == "8":
            shop()
        elif dest == "0":
            menu = True
            play = False

    # CLOCK AND TIME
        clock += 1
        if clock >= 12:
            time = "PM"
        if clock > 24:
            clock = 0
            time = "AM"