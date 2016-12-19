
import keras as k
from keras.layers import Dropout, Input, merge, Dense
from keras.layers.core import Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.models import Model 
from keras.optimizers import SGD

#print k.__version__

from numpy import *
import numpy as np
import sys
from functions import *
import time

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


weights = [load('weights/conv_weights0.npy'), load('weights/conv_weights1.npy')]
model.layers[1].set_weights(weights)

weights = [load('weights/dense_weights0.npy'), load('weights/dense_weights1.npy')]
model.layers[12].set_weights(weights)    

#learning_rate = 0.1
#momentum = 0.8
#sgd = SGD(lr=learning_rate, momentum=momentum, nesterov=False)
#model.compile(loss='binary_crossentropy', optimizer=sgd)
model.compile(loss='binary_crossentropy', optimizer='rmsprop')

#print model.summary()

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


state = zeros([2,6,7], dtype=int)

#p = random.randint(0,1)
p = 1

game_over = False

import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
stdscr.refresh()

y = 10
x = 50

yo = y - 1
xo = x + 2

arrow_col = 0


def drawboardcurses(state, x, y, stdscr):

    stdscr.refresh()
    stdscr.addstr(y, x,     ' ___ ___ ___ ___ ___ ___ ___ ')
    stdscr.addstr(y+1, x,   '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+2, x,   '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+3, x,   '|___|___|___|___|___|___|___|')    
    stdscr.addstr(y+4, x,   '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+5, x,   '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+6, x,   '|___|___|___|___|___|___|___|')    
    stdscr.addstr(y+7, x,   '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+8, x,   '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+9, x,   '|___|___|___|___|___|___|___|')    
    stdscr.addstr(y+10, x,  '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+11, x,  '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+12, x,  '|___|___|___|___|___|___|___|')    
    stdscr.addstr(y+13, x,  '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+14, x,  '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+15, x,  '|___|___|___|___|___|___|___|')    
    stdscr.addstr(y+16, x,  '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+17, x,  '|   |   |   |   |   |   |   |')
    stdscr.addstr(y+18, x,  '|___|___|___|___|___|___|___|')  
    

    for r in range(6):
       for c in range(7):
           if(state[0,r,c]==1):
               stdscr.addstr(y+2+3*r,x+2+4*c,'O')
            
    for r in range(6):
       for c in range(7):
           if(state[1,r,c]==1):
               stdscr.addstr(y+2+3*r,x+2+4*c,'X')
                

while(not game_over and sum(state)<42):
    
    if(p==1): #human move
        key = ''
        if key == ord('q'):
            break
        
        while key != curses.KEY_DOWN:

            key = stdscr.getch()

            if key == curses.KEY_RIGHT:
                if(xo < x + 2 + 4*6):
                    xo += 4
                    arrow_col += 1
            if key == curses.KEY_LEFT:
                if(xo > x + 2): 
                    xo -= 4
                    arrow_col -= 1

            drawboardcurses(state, x, y, stdscr)
                    
            stdscr.addstr(y-2 ,x+2, '                             ')
            stdscr.addstr(y-1 ,x+2, '                             ')
            stdscr.addstr(yo-1,xo,'|')
            stdscr.addstr(yo,  xo, 'v')   
            
            stdscr.addstr(35,25, 'cursor -> ')
            stdscr.refresh()

        next_row = 5-sum(state[:,:,arrow_col])
        state[1,next_row,arrow_col] = 1

        p = (p+1)%2
        
    else: #p==0 computer's move

        #find available moves and generate available states
        available_states = find_available_states(state)
        NN_input = prepare_NN_input(available_states)
        
        #predict on available states. save states and predictions.
        pred = model.predict(NN_input)
        #print 'predictions are : ',y

        #update state
        best_move = argmax(pred)
        state = available_states[best_move]

        p = (p+1)%2

        time.sleep(0.5)
        
    drawboardcurses(state, x, y, stdscr)
    stdscr.refresh()
    game_over = check_game_over_current(state)


while key != curses.KEY_DOWN:
    key = stdscr.getch()

    stdscr.addstr(35,25, 'press down to escape')

time.sleep(5.0)
    
curses.endwin()




