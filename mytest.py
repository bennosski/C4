
from numpy import *
import time
import subprocess
from functions import *

def draw_board(state):

    print ' _______ '

    for r in range(6):
        line = '|'
        for c in range(7):
            if(state[0,r,c]==0 and state[1,r,c]==0):
                line += " "
            elif(state[0,r,c]==1):
                line += u'\u2605'
            elif(state[1,r,c]==1):
                line += u'\u2622'
        line += '|'
        print line
    print ' ------- '


def draw_board2(state):

    print "hello"

    line = '___'
    for c in range(6):
        line += ' ___'
    print line+'\''
       
    for r in range(6):
        line = '|'
        for c in range(7):
            line += '   |'
        print line
        
        line = '|'
        for c in range(7):
            if(state[0,r,c]==0 and state[1,r,c]==0):
                line += '   |'
            elif(state[0,r,c]==1):
                line += ' '+u'\u2605'+' |'
            elif(state[1,r,c]==1):
                line += ' '+u'\u2622'+' |'
        print line

        line = '|'
        for c in range(7):
            line += '___|'
        print line
        

state = zeros([2,6,7], dtype=int)
state[1,5,1] = 1
state[0,4,1] = 1
state[1,3,1] = 1
state[0,5,2] = 1


subprocess.call(["printf", "\033c"])

draw_board2(state)

time.sleep(1.0)

subprocess.call(["printf", "\033c"])

draw_board2(state)



test()


time.sleep(1.0)

myinput = prepare_input(state)

print myinput[:,:,0]
print "end "
print myinput[:,:,1]
print "end"
print myinput[:,:,2]
print "end"
print myinput[:,:,3]
