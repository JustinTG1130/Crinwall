import os
from player import *
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

def map():
                # = 0       x = 1       x = 2       x = 3       x = 4
    map = [["warehouse",   "street",    "house",   "temple",   "house"],    # y = 0
           [    "house",   "street", "townhall",   "street",  "jewler"],    # y = 1
           [    "house",   "street",    "tower",   "street",   "house"],    # y = 2
           [      "inn",   "street",   "street",   "street",   "house"],    # y = 3
           [     "shop",   "street",   "stables",   "house",   "house"]]    # y = 4
    
    y_len = len(map) -1
    x_len = len(map[0]) -1
    
    tile ={
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
        "shop": {
            "t": "SHOP",
            "e": False}}