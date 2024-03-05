from functions import clear, draw, draw_long

def shop():
    shop = True
    while shop:
        clear()
        string1 = "Yes".center()
        draw_long()
        print("  1 - UPGRADE WEAPON")
        print("  2 - UPGRADE ARMOR")
        print("  3 - UPGRADE WEAPON")
        print("  4 - POTION OF HEALING")
        print("  5 - GREATER POT OF HEALING")
        print("  0 - LEAVE")
        print(string1)
        draw_long()

        choice = input("# ")

        if choice == "0":
            shop = False