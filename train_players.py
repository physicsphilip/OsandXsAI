#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Os and Xs

Use TensorFlow to create an AI trained to
decide winning move using penultimate game grids.
"""
from players import *
from game import *


def TrainPenAI(player1,player2,N_train,N_test):
    
    #Generate training data
    results_train = playmanygames(player1,player2,N_train)
    penultimate_train = results_train.allpenultimates
    
    #Let's remove turns that resulted in a draw
    penultimate_train_nodraws = np.delete(penultimate_train, np.where(penultimate_train[:,10] == 0)[0], axis=0)
    penultimate_train_x = penultimate_train_nodraws[:,0:9]
    penultimate_train_y = penultimate_train_nodraws[:,9]
    
    
    #Generate test data
    results_test = playmanygames(player1,player2,N_test)
    penultimate_test = results_test.allpenultimates
    
    #Once again, remove turns that resulted in a draw
    penultimate_test_nodraws = np.delete(penultimate_test, np.where(penultimate_test[:,10] == 0)[0], axis=0)
    penultimate_test_x = penultimate_test_nodraws[:,0:9]
    penultimate_test_y = penultimate_test_nodraws[:,9]
    
    #Time for the ML bit
    import tensorflow as tf
    from tensorflow import keras
    
    #create model
    model_pen = keras.Sequential([
        #keras.layers.Dense(128, input_shape=(penultimate_train_x.shape[1],), activation='relu'),  # hidden layer (2)
        keras.Input(shape=(9,)),
        keras.layers.Dense(128, activation='relu'),  # hidden layer (2)
        keras.layers.Dense(9, activation='softmax') # output layer (3)
    ])
    
    #compile model
    model_pen.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    #train model
    model_pen.fit(penultimate_train_x, penultimate_train_y, epochs=10)
    
    ##testing
    #test_loss, test_acc = model_pen.evaluate(penultimate_test_x, penultimate_test_y, verbose=1) #verbose = how much printed in console
    
    model_pen.save("OXAIPenMod.keras")
