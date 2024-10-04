#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Os and Xs

Main file

Must be in same folder as
    players.py (for player classes)
    game.py (for game classes and functions)
    plotting.py (for plotting function)

Available player classes are
    human
    AIrandom
    AIsequential
    AIMLpen

"""

from players import *
from game import *

#Define the player types
player1 = AIMLpen()
player2 = AIrandom()

# #How many games?
# N_train = 10000
# N_test = 200

# #Train AI based on penultimate board position
# from train_players import *
# TrainPenAI(player1, player2, N_train, N_test)


results = playmanygames(player1, player2, 1000)

#Plot results
from plotting import *
plotgameresults(player1,player2,results)
