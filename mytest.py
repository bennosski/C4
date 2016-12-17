
from numpy import *

state = zeros([6,7,2])
state[1,1,1] = 1
state[5,4,0] = 1

draw_board(state)



def draw_board(state):

    print ' ______ '

    for r in range(6):
        print '|',
        for c in range(7):
            if(state[0,r,c]==0 and stae[1,r,c]==0):
                print " "
            elif(state[0,r,c]==1):
                print u'\u2605'
            elif(state[1,r,c]==1):
                print u'\u2622'
        print '|'

    print ' ------ '

    
    
