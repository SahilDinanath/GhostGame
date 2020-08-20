import math
import os
import sys
from random import choice
from random import randint
#It's Sahil Dinanath
# --------------------------------------------------------------------------- #

room = 1
lvl = 0
max_hp = 10
hp = max_hp
str = 5
dex = 5
hor = 5
exp = 0
limit = 10

# --------------------------------------------------------------------------- #

def level_up():
    global lvl
    global limit
    global max_hp
    global hp
    global str
    global dex
    global hor
    lvl = lvl + 1
    limit = limit * 2
    max_hp = max_hp + lvl * 5
    hp = max_hp
    str = str + randint(lvl, lvl * 2)
    dex = dex + randint(lvl, lvl * 2)
    hor = hor + randint(lvl, lvl * 2)
    print(f"\n\tYou leveled up to level {lvl}")
    print(f"""
        ____________________________________________

                            - Stats -

        ____________________________________________
            Level: -{lvl}-
            EXP: [{exp} / {limit}]

            Willpower: [{hp} / {max_hp}]
            Strength: {str}
            Dexterity: {dex}
            Horror: {hor}
        ____________________________________________
    """)

# --------------------------------------------------------------------------- #

def win():
    global exp
    exp = exp + room * 2
    if exp >= limit:
        level_up()
    else:
        print(f"\n\tExp: [{exp} / {limit}]")

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
    damage = room / 2
    global hp
    if randint(1, str) < room / 2:
        hp = hp - damage
        print("\n\tYou attacked the ghost!")
        print("\n\tThe attack missed...")
        print("\n\tThe ghost attacked.")
        print(f"\n\tYou took {damage} damage.")
        print(f"\n\tHP: {hp}")
        if hp <= 0:
            hp = 0
        else:
            battle()
    else:
        print("\n\tYou attacked the ghost!")
        print("\n\tIt vanished")
        print("\n\tYou won!")
        win()

# --------------------------------------------------------------------------- #

def fright():
    damage = room / 2
    global hp
    if hor > room:
        print("\nWow you managed to scare the ghost off...")
    else:
        hp = hp - damage
        print("\n\tYou attempted to scare the ghost...and failed...")
        print("\n\tThe ghost attacked.")
        print(f"\n\tYou took {damage} damage.")
        print(f"\n\tHP: {hp}")
        if hp <= 0:
            hp = 0
        else:
            battle()

# --------------------------------------------------------------------------- #

def flight():
    damage = room / 2
    global hp
    if dex > room:
        print("\n\tYou decided to run away from the cute ghost.")
    else:
        hp = hp - damage
        print("\n\tYou attempted to run away...and failed...")
        print("\n\tThe ghost attacked.")
        print(f"\n\tYou took {damage} damage.")
        print(f"\n\tHP: {hp}")
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
            Level: -{lvl}-
            EXP: [{exp} / {limit}]

            Willpower: [{hp} / {max_hp}]
            Strength: {str}
            Dexterity: {dex}
            Horror: {hor}
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
    global room
    global hp
    while hp > 0:
        print(f"""
        ____________________________________________

                        - Room {room} -

        --------------------------------------------
                        Choose a Door

                    > 1
                    > 2
                    > 3
                                        > Options
        ____________________________________________
        """)

        doors = ["1", "2", "3"]
        ghost_door = choice(doors)
        chance = randint(1, 5)
        pick = input("> ")
        if pick != "1" and pick != "2" and pick != "3" and pick != "options":
            print("Enter a valid option")
        elif pick == "options":
            options()
        elif pick == ghost_door:
            room = room + 1
            battle()
        elif chance == 1:
            room = room + 1
            hp = hp + randint(room, room * 2)
            if hp > max_hp:
                hp = max_hp
                print("\n\tYou found souls!")
                print(f"\n\tYour Willpower remained at {hp}")
            else:
                print("\n\tYou found souls!")
                print(f"\n\tYour Willpower is now {hp}")
        elif chance != 1:
            print("\n\tYou safely made it into the next room")
            room = room + 1
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
    global quit
    while hp > 0:
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
