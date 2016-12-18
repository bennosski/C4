import keras as k
from keras.layers import Dropout, Input, merge, Dense
from keras.layers.core import Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.models import Model 

print k.__version__

from numpy import *
from functions import *

import h5py

input2b2 = Input(shape=(49,1), dtype='float32', name='input2b2')
dropout2b2 = (Dropout(0.2))(input2b2)
f2b2 = (Flatten())(dropout2b2)

input4b1 = Input(shape=(26,1), dtype='float32', name='input4b1')
dropout4b1 = (Dropout(0.2))(input4b1)
f4b1 = (Flatten())(dropout4b1)

main_input = Input(shape=(2,6,7), dtype='float32', name='main_input')
conv = (Convolution2D(100, 3, 3, border_mode="valid",
                                 activation="relu",
                                 subsample=(1,1)))(main_input)
pool = (MaxPooling2D(pool_size=(4,5), strides=(1,1), border_mode='valid',dim_ordering='th'))(conv)
dropout = (Dropout(0.2))(pool)
f = (Flatten())(dropout)

m = merge([f2b2, f4b1, f], 'concat')

myoutput = (Dense(input_dim=49+26+100, output_dim=1, activation='sigmoid'))(m)

model = Model(input=[input2b2, input4b1, main_input], output=myoutput)

model.compile(loss='binary_crossentropy', optimizer='rmsprop')

print model.summary()

'''
state = zeros([2,6,7], dtype=int)
state[1,5,1] = 1
state[0,4,1] = 1
state[1,3,1] = 1
state[0,5,2] = 1
states = []
states.append(state)
NN_input = prepare_NN_input(states)
y = model.predict(NN_input, verbose=1)
print "the prediction is ", y
'''

#why better to do with tensorflow in the future:
#easier to convert to numpy calculation
#custom convolution filters with some zero weights


#now setup the learning procedure
state = zeros([2,6,7], dtype=int)

player = 0
n_games = 1

for game in range(n_games):
    print "    starting game ",game

    turn = 0
    game_over = False
    iter_count = 0
    
    while(not game_over and iter_count<42):
        #find available moves and generate available states
        available_states = find_available_states(state)
        NN_input = prepare_NN_input(available_states)
        
        #predict on available states. save states and predictions.
        y = predict(NN_input, verbose=1)
        print 'predictions are : ',y

        #update state
        best_move = argmax(y)
        state = available_states[best_move]
        
        turn += 1
        player = (player + 1)%2
        
        #flip board
        state_copy = state.copy()
        state[0,:,:] = state_copy[1,:,:]
        state[1,:,:] = state_copy[0,:,:]

        #check for game over
        game_over = check_game_over(state)

        iter_count += 1

        
    #now learn
    #generate the true y_scores for each state in each turn
    #perform learning on the full game as a batch. learn for 1 epoch only. 














