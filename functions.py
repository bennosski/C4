
from numpy import *


def test():
    x = linspace(0,10,11)

    print 'test ',x[4:5]


def prepare_input(state):
    
    output = zeros([49,5,6])
    m = zeros([2,2,2])
    
    for r in range(5):
        for c in range(6):
            m = state[:,r:r+1,c:c+1]
            

    
