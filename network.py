
import keras as k
from keras.layers import Dropout, Input, merge, Dense
from keras.layers.core import Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.models import Model 
from keras.optimizers import SGD

print k.__version__

from numpy import *
import numpy as np
from functions import *
import sys

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


if(sys.argv[1]=='load'):
    weights = [load('weights/conv_weights0.npy'), load('weights/conv_weights1.npy')]
    model.layers[1].set_weights(weights)

    weights = [load('weights/dense_weights0.npy'), load('weights/dense_weights1.npy')]
    model.layers[12].set_weights(weights)    

#learning_rate = 0.1
#momentum = 0.8
#sgd = SGD(lr=learning_rate, momentum=momentum, nesterov=False)
#model.compile(loss='binary_crossentropy', optimizer=sgd)
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
n_games = 100

state = zeros([2,6,7], dtype=int)
prev_state = zeros([2,6,7], dtype=int)

n_samestate = 0
max_n_samestate = 0

for game in range(n_games):
    prev_state = state.copy()
    state = zeros([2,6,7], dtype=int)
    player = 0
    
    print "\n\n\n\n"
    print "    starting game ",game

    turn = 0
    game_over = False
    iter_count = 0

    turns_states = []
    turns_predictions = []
    turns_moves = []
    
    while(not game_over and sum(state)<42):
        #find available moves and generate available states
        available_states = find_available_states(state)
        NN_input = prepare_NN_input(available_states)
        
        #predict on available states. save states and predictions.
        y = model.predict(NN_input, verbose=1)
        #print 'predictions are : ',y

        #update state
        best_move = argmax(y)
        state = available_states[best_move]

        turns_states.append(NN_input)
        turns_predictions.append(y)
        turns_moves.append(best_move)
                
        #flip board
        state_copy = state.copy()
        state[0,:,:] = state_copy[1,:,:]
        state[1,:,:] = state_copy[0,:,:]

        iter_count += 1
        turn += 1
        player = (player + 1)%2

        #check for game over
        game_over,state = check_game_over(state)
               
    draw_board(state) 

    '''
    same_state = True
    for i in range(2):
        for j in range(6):
            for k in range(7):
                if(state[i,j,k] != prev_state[i,j,k]):
                    same_state = False
    '''
    
    if(not ((prev_state - state).any() != 0)):
        print 'state not updating n_samestate ',n_samestate
        n_samestate += 1
        print prev_state-state

        if(n_samestate > max_n_samestate):
            max_n_samestate = n_samestate
        
        if(n_samestate>10):
            break
    else:
        n_samestate = 0
        
    #if game is over then turn = number of turns played
    #check tie separately (sum(states)=42)
    if(sum(state)==42 and not game_over):
        print 'tie. Not learning'
        continue
    
    #now learn based on on each turn
    #generate the true y_scores for each state in each turn
    #perform learning on the full game as a batch. learn for 1 epoch only. 

    fractions = linspace(0.05, 1, turn)

    loser = True
    for t in range(turn-1,-1,-1): #from turn-1 to 0 loop
        print 'learning for turn',t
        
        m = turns_moves[t]
        preds = turns_predictions[t]
        p = preds[m]
        
        for i in range(len(preds)):
            print preds[i],
        print ''
        
        if(loser):
            change = p*fractions[t]
            pnew = p - change
            loser = False
        else:
            change = (1.0-p)*fractions[t]
            pnew = p + change
            loser = True
        '''    
        sum_p = sum(preds) - p
        scale = (sum_p - change)/sum_p
        
        p_true = scale*preds
        p_true[m] = pnew
        '''
        
        p_true = preds.copy()
        p_true[m] = pnew
        
        for i in range(len(p_true)):
            print p_true[i],
        print ''
        
        #model.fit(turns_states[t], p_true, nb_epoch=1, verbose=1)
        model.train_on_batch(turns_states[t], p_true)

#draw_board(state) 


print '\n\n max_n_samestate',max_n_samestate

weights = model.layers[1].get_weights()
for i in range(len(weights)):
    print shape(weights[i])
save("weights/conv_weights0.npy", weights[0])
save("weights/conv_weights1.npy", weights[1])
    
print ""

weights = model.layers[12].get_weights()
for i in range(len(weights)):
    print shape(weights[i])
save("weights/dense_weights0.npy", weights[0])
save("weights/dense_weights1.npy", weights[1])



    










