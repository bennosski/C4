
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

p = random.randint(0,1)

game_over = False

while(not game_over)












