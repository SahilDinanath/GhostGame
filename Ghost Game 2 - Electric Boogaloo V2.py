import math
import os
import sys
from random import choice
from random import randint

# --------------------------------------------------------------------------- #
class ghost_game:

    room = 1
    lvl = 0
    max_hp = 10
    hp = max_hp
    str = 5
    dex = 5
    hor = 5
    exp = 0
    limit = 10

def level_up():
    ghost_game.lvl = ghost_game.lvl + 1
    ghost_game.limit = ghost_game.limit * 2
    ghost_game.max_hp = ghost_game.max_hp + ghost_game.lvl * 5
    ghost_game.hp = ghost_game.max_hp
    ghost_game.str = ghost_game.str + randint(ghost_game.lvl, ghost_game.lvl * 2)
    ghost_game.dex = ghost_game.dex + randint(ghost_game.lvl, ghost_game.lvl * 2)
    ghost_game.hor = ghost_game.hor + randint(ghost_game.lvl, ghost_game.lvl * 2)
    print(f"\n\tYou leveled up to level {ghost_game.lvl}")
    print(f"""
        ____________________________________________

                            - Stats -

        ____________________________________________
            Level: -{ghost_game.lvl}-
            EXP: [{ghost_game.exp} / {ghost_game.limit}]

            Willpower: [{ghost_game.hp} / {ghost_game.max_hp}]
            Strength: {ghost_game.str}
            Dexterity: {ghost_game.dex}
            Horror: {ghost_game.hor}
        ____________________________________________
    """)

# --------------------------------------------------------------------------- #
def win():
    ghost_game.exp = ghost_game.exp + ghost_game.room * 2
    if ghost_game.exp >= ghost_game.limit:
        level_up()
    else:
        print(f"\n\tExp: [{ghost_game.exp} / {ghost_game.limit}]")

# --------------------------------------------------------------------------- #

def lose():
    print("""

        ____________________________________________

                        - You Died... -

        ____________________________________________
                    > Play Again?
        ____________________________________________
    """)
    sys.exit()

# --------------------------------------------------------------------------- #

def fight():
    ghost_game.damage = ghost_game.room / 2
    if randint(1, ghost_game.str) < ghost_game.room / 2:
        ghost_game.hp = ghost_game.hp - ghost_game.damage
        print("\n\tYou attacked the ghost!")
        print("\n\tThe attack missed...")
        print("\n\tThe ghost attacked.")
        print(f"\n\tYou took {ghost_game.damage} damage.")
        print(f"\n\tHP: {ghost_game.hp}")
        if ghost_game.hp <= 0:
            ghost_game.hp = 0
        else:
            battle()
    else:
        print("\n\tYou attacked the ghost!")
        print("\n\tIt vanished")
        print("\n\tYou won!")
        win()

# --------------------------------------------------------------------------- #

def fright():
    ghost_game.damage = ghost_game.room / 2
    if ghost_game.hor > ghost_game.room:
        print("\nWow you managed to scare the ghost off...")
    else:
        ghost_game.hp = ghost_game.hp - ghost_game.damage
        print("\n\tYou attempted to scare the ghost...and failed...")
        print("\n\tThe ghost attacked.")
        print(f"\n\tYou took {ghost_game.damage} damage.")
        print(f"\n\tHP: {ghost_game.hp}")
        if ghost_game.hp <= 0:
            ghost_game.hp = 0
        else:
            battle()

# --------------------------------------------------------------------------- #

def flight():
    ghost_game.damage = ghost_game.room / 2
    if ghost_game.dex > ghost_game.room:
        print("\n\tYou decided to run away from the cute ghost.")
    else:
        ghost_game.hp = ghost_game.hp - ghost_game.damage
        print("\n\tYou attempted to run away...and failed...")
        print("\n\tThe ghost attacked.")
        print(f"\n\tYou took {ghost_game.damage} damage.")
        print(f"\n\tHP: {ghost_game.hp}")
        if hp <= 0:
            hp = 0
        else:
            battle()

# --------------------------------------------------------------------------- #

def battle():
    print("""
        ____________________________________________

             - You Encountered a Spooky Ghost! -

        --------------------------------------------
            What do you want to do?

                    > 1: Fight
                    > 2: Fright
                    > 3: Flight
        ____________________________________________
    """)
    decision = input("> ")

    if decision == "1":
        fight()
    elif decision == "2":
        fright()
    elif decision == "3":
        flight()
    else:
        print("\n\tEnter a valid option.")
        battle()

# --------------------------------------------------------------------------- #

def options():
    print(f"""
        ____________________________________________

                        - Options -

        --------------------------------------------
                    > 1: Check Stats
                    > 2: Back to Game
                    > 3: Quit to Title
        ____________________________________________
    """)
    option = input("> ")
    if option == "1":
        print(f"""
        ____________________________________________

                        - Stats -

        --------------------------------------------
            Level: -{ghost_game.lvl}-
            EXP: [{ghost_game.exp} / {ghost_game.limit}]

            Willpower: [{ghost_game.hp} / {ghost_game.max_hp}]
            Strength: {ghost_game.str}
            Dexterity: {ghost_game.dex}
            Horror: {ghost_game.hor}
        ____________________________________________
        """)
    elif option == "2":
        play()
    elif option == "3":
        menu()
    else:
        print("\n\tEnter a valid option.")

# --------------------------------------------------------------------------- #

def play():
    while ghost_game.hp > 0:
        print(f"""
        ____________________________________________

                        - Room {ghost_game.room} -

        --------------------------------------------
                        Choose a Door

                    > 1
                    > 2
                    > 3
                                        > Options
        ____________________________________________
        """)

        ghost_game.doors = ["1", "2", "3"]
        ghost_door = choice(ghost_game.doors)
        chance = randint(1, 5)
        pick = input("> ")
        if pick != "1" and pick != "2" and pick != "3" and pick != "options":
            print("Enter a valid option")
        elif pick == "options":
            options()
        elif pick == ghost_door:
            ghost_game.room = ghost_game.room + 1
            battle()
        elif chance == 1:
            ghost_game.room = ghost_game.room + 1
            ghost_game.hp = ghost_game.hp + randint(ghost_game.room, ghost_game.room * 2)
            if ghost_game.hp > ghost_game.max_hp:
                ghost_game.hp = ghost_game.max_hp
                print("\n\tYou found souls!")
                print(f"\n\tYour Willpower remained at {ghost_game.hp}")
            else:
                print("\n\tYou found souls!")
                print(f"\n\tYour Willpower is now {ghost_game.hp}")
        elif chance != 1:
            print("\n\tYou safely made it into the next room")
            ghost_game.room = ghost_game.room + 1
    else:
        lose()

# --------------------------------------------------------------------------- #

def help_menu():
    print(f"""
        ____________________________________________

                        - Help Menu -

        --------------------------------------------
            Literally just pick an option.
            Baka idiot.
        ____________________________________________
    """)
    menu()

# --------------------------------------------------------------------------- #

def menu():
    print("""
        ____________________________________________

                  - Welcome to Ghost Game -

        --------------------------------------------
                    > Play
                    > Help
                    > Quit
        ____________________________________________
    """)
    while True:
        start = input("> ").lower()
        if start == "play":
            play()
        elif start == "help":
            help_menu()
        elif start == "quit":
            sys.exit()
        else:
            print("\n\tEnter a valid option.")
menu()
# --------------------------------------------------------------------------- #
