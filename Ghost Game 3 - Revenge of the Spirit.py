import math
import os
import sys
from random import choice
from random import randint

# --------------------------------------------------------------------------- #

# Player Setup #
class player:
    def __init__(self):
        self.name = ""
        self.lvl = 1
        self.hp = 10
        self.str = 5
        self.dex = 5
        self.drd = 5
        self.exp = 0
my_player = player()

# --------------------------------------------------------------------------- #
