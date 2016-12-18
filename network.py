

import keras as k
from keras.layers import Dropout, Input
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.models import Model 

print k.__version__

from numpy import *
from functions import *

state = zeros([2,6,7], dtype=int)
state[1,5,1] = 1
state[0,4,1] = 1
state[1,3,1] = 1
state[0,5,2] = 1

myinput = prepare_input(state)

main_input = Input(shape=(49,5,6), dtype='float32', name='main_input')

conv = (Convolution2D(100, 2, 2, border_mode="valid",
                                 activation="relu",
                                 subsample=(1,1)))(main_input)
        
pool1 = (MaxPooling2D(pool_size=(1,1), strides=(1,1), border_mode='valid',dim_ordering='th'))(conv)
        
dropout = (Dropout(0.2))(pool1)

model = Model(input=main_input, output=dropout)

model.compile(loss='binary_crossentropy', optimizer='rmsprop')

print model.summary()









