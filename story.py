from functions import draw, draw_ex_long, draw_long, clear
from player import player
def intro():
    draw_ex_long()
    print(f"""    {player.name}.
    I'm sending you to the city Crinwall. 
    There has been talk of a plot to assassinate 
    the High Regent's only heir when he arrives.
    
    Your task is to find out who's planning this and put a stop 
    to them.
    It is of the upmost importance that you DO NOT FAIL! For if 
    you do, chaos and infighting will insue.
    Rent a room at the inn(X: 0, Y: 3), and talk to the people there.
    
    ~ Grandmaster Daraphil""")
    draw_ex_long()
    input("# ")


# Beginning
def innkeeper():
    talk = True
    if player.story_progress >= 0:
        while talk:
            clear()
            draw_long()
            print("   What do you want to talk about?")
            # Dialog options
            draw_long()
            print("   1 - What are the rumors around town?")
            print("   2 - Tell me about the town.")
            if player.story_progress == 1:
                print("   3 - About the Blackwater Syndicate")
            print("   0 - Goodbye!")
            draw_long()
            choice = input("# ")

            if choice == "1":
                clear()
                draw_ex_long()
                print("   Well.. Tristen over there's been pretty down.")
                print("   His shop was broken into the other week,")
                print("   they say that it had something to do with..")
                print("   (*He looks around. Then says in a whisper*)")
                print("   the Blackwater Syndicate.\n")
                print("   If you want to know more, I'd go talk to him.")
                draw_ex_long()
                input("# ")
                if player.story_progress == 0:

                    player.story_progress = 1
            elif choice == "2":
                clear()
                draw_ex_long()
                print("  Crinwall is the center of trade in the realm. \n")
                print("  The people are tough however, you have to be")
                print("  *He quitetly says*")
                print("  with the Blackwater Syndicate about.")
                draw_ex_long()
                input("# ")
                if player.story_progress == 0:
                    player.story_progress = 1
            elif choice == "3":
                clear()
                draw_ex_long()
                print("   *A drop bead of sweat runs down his face*")
                print("   They're a group of thieves and scoundrels. Good for nothing.")
                print("   But they have a hold on this city and they aren't letting go.")
                print("   If you're smart, you wont mess with them. If you have a death")
                print("   wish however, start by talking to Tristen over there.")
                draw_ex_long()
                input("# ")
            elif choice == "0":
                talk = False

def tristen():
    if player.story_progress == 1:
        clear()
        talk = True
        draw_ex_long()
        print("   *He looks up at you and says*")
        print("   Look this isn't a good time right now, just leave me be.")
        draw_ex_long()
        input("# ")
        while talk:
            clear()
            draw_long()
            print("   1 - I heard you're having a problem?")
            print("   0 - Goodbye!")
            draw_long()

            choice = input("# ")
            if choice == "1":
                clear()
                draw_ex_long()
                print("   Yep.. Blackwater Syndicate. Got myself owing them a debt.")
                print("   They came in my store a week ago saying they wouldn't ransack")
                print("   the place if I continue to pay them. But now they increased")
                print("   what I owe.. and I don't have that kind of money.")
                draw_ex_long()
                print("   If you want to help, I own a jewlery store on the East side")
                print("   of town. We can maybe set an ambush for them.")
                draw_ex_long()
                input("# ")
                player.story_progress = 2
            elif choice == "0":
                talk = False
    elif player.story_progress == 2:
        draw_ex_long()
        print("   I'm glad you came. Alright, just hide behind the counter.")
        draw_ex_long()
        input()
        clear()
        draw_ex_long
        print("   *You hide behind the counter, and Tristen goes into the back room.")
        print("   A man dressed in rugged black leather armor comes in the front door*")
        draw_ex_long()
        input("FIGHT")