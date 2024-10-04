#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Os and Xs

Player classes
"""
import numpy as np
import random #for random numbers
import tensorflow as tf #for ML trained AI
from tensorflow import keras #for ML trained AI

#player class
class player:
    description = "Player (base class)"

#human player class
class human(player):
    description = "Human player"
    def makemove(self,currentgrid):
        check_input = 0
        while check_input == 0:
            choice = int(input("Your turn: "))
            if currentgrid[choice] == 0:
                currentgrid[choice] = 1
                check_input = 1
            else:
                print("Invalid choice.")
        return choice
    
#AI (random) class
class AIrandom(player):
    description = "Random AI"
    def makemove(self,currentgrid):
        check_input = 0
        while check_input == 0:
            choice = random.randint(0,8)
            if currentgrid[choice] == 0:
                currentgrid[choice] = 1
                check_input = 1
        return choice

#AI (sequential) class    
class AIsequential(player):
    description = "Sequential AI"
    def makemove(self,currentgrid):
        check_input = 0
        choice = 0
        while check_input == 0:
            if currentgrid[choice] == 0:
                currentgrid[choice] = 1
                check_input = 1
            else:
                choice = choice + 1
        return choice

#AI (ML trained on penultimate move) class

model_pen = keras.models.load_model("OXAIPenMod.keras") #load model for AI

class AIMLpen(player):
    description = "ML trained on penultimate move"
    def makemove(self,currentgrid):
        check_input = 0
        
        #make predict probabilities of each move resulting in victory
        grid_for_prediction = np.zeros((2,9))
        grid_for_prediction[0,0:9] = currentgrid[0:9]
        probabilities = model_pen.predict(grid_for_prediction,verbose=0)
        #choose position most likely to result in victory
        choice = np.argmax(probabilities[0,:])
                
        while check_input == 0:
            if currentgrid[choice] == 0:
                currentgrid[choice] = 1
                check_input = 1
            else:
                #if AI picked an already-occupied slot, choose another at random
                choice = random.randint(0,8)
        return choice

