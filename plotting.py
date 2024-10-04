#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Os and Xs

Plot results
"""
import numpy as np
import matplotlib.pyplot as plt

def plotgameresults(player1,player2,results):
    #Extract data for analysis
    allvictories = results.allvictories
    allturns = results.allturns
    allpositions = results.allpositions
    
    #plot two vertically stacked graphs

    #what is the relative frequency of 1, 2 and draw?

    result_outcomes = np.unique(allvictories)
    result_outcomes_str = ["Player 1","Player 2","Tie game"]
    #result_outcomes_freq = np.unique(allvictories, return_counts=True)[1]
    result_outcomes_freq = np.zeros(3)
    result_outcomes_freq[0] = np.count_nonzero(allvictories == 1)
    result_outcomes_freq[1] = np.count_nonzero(allvictories == 2)
    result_outcomes_freq[2] = np.count_nonzero(allvictories == 0)


    ax1 = plt.subplot(2, 1, 1)
    plt.bar(result_outcomes_str,result_outcomes_freq);
    plt.xlabel("Game outcomes")
    ax1.set_title(player1.description + " vs " + player2.description)
    #how many turns does it take to reach game over?
    result_turns = np.unique(allturns)
    result_turns_freq = np.unique(allturns, return_counts=True)[1]
    ax2 = plt.subplot(2, 1, 2)
    plt.bar(result_turns,result_turns_freq);
    plt.xlabel("Turns until endgame")