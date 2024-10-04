#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Os and Xs

Game classes and functions
"""

import numpy as np


"""
Classes
"""

#Class to return results from a game
class gameresult:
    def __init__(self,victory,turn,positions,penultimate):
        self.victory = victory
        self.turn = turn
        self.positions = positions
        self.penultimate = penultimate

#Class to return results from many games
class manygameresults:
    def __init__(self,allvictories,allturns,allpositions,allpenultimates):
        self.allvictories = allvictories
        self.allturns = allturns
        self.allpositions = allpositions
        self.allpenultimates = allpenultimates

"""
And here are all the functions
"""
#function for printing out grid by converting from integers
#for some reason this is very buggy!
def gridprint(gameiteration):
    
    printing = ["_","_","_","_","_","_","_","_","_"]
    
    for x in gameiteration:
   #     if gameiteration[x] == 0:
   #         printing.append("_")
        if gameiteration[x] == 1:
            printing[x] = "O"
        elif gameiteration[x] == 2:
            printing[x] = "X"

    print("\n\t |" + printing[0] + "|" + printing[1] + "|" + printing[2] + "|\n\t |" + printing[3] + "|" + printing[4] + "|" + printing[5] + "|\n\t |" + printing[6] + "|" + printing[7] + "|" + printing[8] + "|")
    #print("\n\t |" + str(gameiteration[0]) + "|" + str(gameiteration[1]) + "|" + str(gameiteration[2]) + "|\n\t |" + str(gameiteration[3]) + "|" + str(gameiteration[4]) + "|" + str(gameiteration[5]) + "|\n\t |" + str(gameiteration[6]) + "|" + str(gameiteration[7]) + "|" + str(gameiteration[8]) + "|")

#function for printing out grid from gameprinting
def gridprintv2(gamelist):
    print("\n\t |" + gamelist[0] + "|" + gamelist[1] + "|" + gamelist[2] + "|\n\t |" + gamelist[3] + "|" + gamelist[4] + "|" + gamelist[5] + "|\n\t |" + gamelist[6] + "|" + gamelist[7] + "|" + gamelist[8] + "|")


#function for checking victory conditions
def victorycheck(gameiteration,turncount):
    #whose turn is it?
    #player 2 plays when turncount is even
    if (turncount % 2) == 0: #i.e. if turncount/2 has remainder 0
        player = 2
    else:
        player = 1
    
    #row conditions
    if gameiteration[0] < 0 and gameiteration[0] == gameiteration[1] and gameiteration[1] == gameiteration[2]:
        victory = player
    elif gameiteration[3] < 0 and gameiteration[3] == gameiteration[4] and gameiteration[4] == gameiteration[5]:
        victory = player
    elif gameiteration[6] < 0 and gameiteration[6] == gameiteration[7] and gameiteration[7] == gameiteration[8]:
        victory = player
    #column conditions
    elif gameiteration[0] < 0 and gameiteration[0] == gameiteration[3] and gameiteration[3] == gameiteration[6]:
        victory = player
    elif gameiteration[1] < 0 and gameiteration[1] == gameiteration[4] and gameiteration[4] == gameiteration[7]:
        victory = player
    elif gameiteration[2] < 0 and gameiteration[2] == gameiteration[5] and gameiteration[5] == gameiteration[8]:
        victory = player
    #diagonal conditions
    #tie game
    elif turncount == 9:
        victory = 0 #3 = tie game
    #game not finished
    else:
        victory = 9
    return victory

#function to play one game
def playgame(player1,player2):
    game = np.zeros((2,9), dtype=np.int8) #define array
    #gameforprinting = [" "," "," "," "," "," "," "," "," "]
    
    turn = 0 #turn counter
    
    victory = 9 #game ends when victory = 1
    
    positions = np.empty((9,1),int) #order of plays
    
    #print("Computer vs computer noughts and crosses.")
    
    while victory == 9:
        ###player 1 turn
        turn = turn + 1
        #print("\nPlayer 1's turn.")
        
        #computer randomly chooses next X position
        choice = player1.makemove(game[turn,:])
        game[turn,choice] = -1
        positions[turn-1] = choice
           
        #check victory
        victory = victorycheck(game[turn,:],turn)
        
        #break loop if victory condition satisfied
        if victory == 1 or victory == 0:
            break
        
        #if no victory, add new row to game matrix
        game = np.r_[game,[game[turn,:]]]
        #multiply game by -1
        game[turn+1,:] = game[turn+1,:] * -1
        
        ###player 2's turn
        turn = turn + 1
        #print("\nPlayer 2's turn.")
        
        #computer randomly chooses next X position
        choice = player2.makemove(game[turn,:])
        game[turn,choice] = -1
        positions[turn-1] = choice
                   
        #check victory
        victory = victorycheck(game[turn,:],turn)
        
        #if no victory, add new row to game matrix
        game = np.r_[game,[game[turn,:]]]
        #multiply game by -1
        game[turn+1,:] = game[turn+1,:] * -1
        
        
    
    #generate "ultimate victor" column
    won_ultimately = np.zeros((9,1))
    won_ultimately_counter=0
    while won_ultimately_counter<9:
        won_ultimately[won_ultimately_counter,0]=(-1)**won_ultimately_counter
        won_ultimately_counter=won_ultimately_counter+1
    
    tie_ultimately = np.zeros((9,1))  
    
    #produce game summary
    if victory == 0:
        summary = np.concatenate((game[0:turn,:], positions[0:turn], tie_ultimately[0:turn]),axis=1)    
    elif victory == 1:
        summary = np.concatenate((game[0:turn,:], positions[0:turn], won_ultimately[0:turn]),axis=1)
    elif victory == 2:
        summary = np.concatenate((game[0:turn,:], positions[0:turn], -1*won_ultimately[0:turn]),axis=1)
    
    penultimate = np.zeros((11,1))
    penultimate[:,0] = summary[turn-1,:]
    
    finishedgame = gameresult(victory,turn,summary,penultimate)
    return finishedgame
    #if (counter % 100) == 0:
    #    print("Completed game " + str(counter) + "/" + str(n_games))

#function to play many games
def playmanygames(player1,player2,n_games):
    ###define arrays to store summary data for each game
    
    #number of games to play
    #n_games = 1000
    
    #order in which grid is filled
    #top-left position is 1, not 0
    #allpositions = np.zeros((9,n_games), dtype=int)
    allpositions = np.zeros((1,11))
    allpenultimates = np.zeros((1,11))
    #outcome of each game
    #1 = player 1 wins, 2 = player 2 wins
    allvictories = np.zeros(n_games, dtype=int)
    #number of turns in each game
    allturns = np.zeros(n_games, dtype=int)
    
    #start of loop for each game
    counter=0
    
    while counter < n_games:
        finishedgame = playgame(player1,player2)
        allvictories[counter] = finishedgame.victory
        #allpositions[0:np.size(finishedgame.positions),counter] = finishedgame.positions
        #allpositions=allpositions+1
        allpositions = np.concatenate((allpositions, finishedgame.positions), axis=0)
        allpenultimates = np.concatenate((allpenultimates, np.transpose(finishedgame.penultimate)), axis=0)
        allturns[counter] = finishedgame.turn
        counter = counter+1
    
    allpositions = np.delete(allpositions, 0, 0)
    allpenultimates = np.delete(allpenultimates, 0, 0)
    
    allgameresults = manygameresults(allvictories,allturns,allpositions,allpenultimates)
    return allgameresults

