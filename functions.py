import os
from player import *
def draw():
    print("<X>--------------------<X>")
def draw_long():
    print("<X>------------------------------<X>")
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