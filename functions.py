
from numpy import *


def test():
    x = linspace(0,10,11)

    print 'test ',x[4:6]

    m = zeros([2,2,2])
    m[1,0,0] = 4
    m[0,1,1] = 1

    print sum(m)
    print amax(m)

    z = zeros(4, dtype=int)
    z[1] = 1
    z[2] = 1
    z[3] = 1

    if(z[1:4] == asarray([1,1,1])):
        print "worked"
    else:
        print "didn't work"
    

def prepare_input2b2(state):
    
    output = zeros([49,5,6])
    m = zeros([2,2,2])
    
    for r in range(5):
        for c in range(6):
            m = state[:,r:r+2,c:c+2]
            sum_m = sum(m)

            index = -1
            
            if(sum_m == 0):
                index = 0

            if(sum_m == 1):
                index = 1

                if(sum(m[:,1,0]) == 1):
                    index += 0
                    index += m[0,1,0]
                else:
                    index += 2
                    index += m[0,1,1]

            if(sum_m == 2):
                index = 5

                if(sum(m[:,1,0])==1 and sum(m[:,1,1])==1):
                    index += 0
                    index += m[0,1,0] + 2*m[0,1,1]
                if(sum(m[:,0,0])==1 and sum(m[:,1,0])==1):
                    index += 4
                    index += m[0,0,0] + 2*m[0,1,0]
                if(sum(m[:,0,1])==1 and sum(m[:,1,1])==1):
                    index += 8
                    index += m[0,0,1] + 2*m[0,1,1]

            if(sum_m == 3):
                index = 17

                if(sum(m[:,0,0]) == 0):
                   index += 0
                   index += m[0,1,0] + 2*m[0,1,1] + 4*m[0,1,0]

                if(sum(m[:,1,0]) == 0):
                   index += 8
                   index += m[0,0,0] + 2*m[0,1,0] + 4*m[0,1,1]
                   
            if(sum_m == 4):
                index = 33
                index += m[0,0,0] + 2*m[0,1,0] + 4*m[0,0,1] + 8*m[0,1,1]                                                          

            if(index==-1):
                print 'error'
                
            print type(index),r,c
            output[index,r,c] = 1.0

    output_max = zeros(49)
    for i in range(49):
        output_max[i] = amax(output[i,:,:])
        
    return output_max

def prepare_input4b1(state):
    output_max = zeros(26)

    m = zeros([2,4])
    for r in range(3):
        for c in range(7):
            m = state[:,r:r+4,c]

            if(m[0,1:4].all() == 1):
                output_max[0] = 1
            if(m[1,1:4].all() == 1):
                output_max[1] = 1

                
    m = zeros([2,4])
    for r in range(6):
        for c in range(4):
            m = state[:,r,c:c+4]

            index = 2
            if(sum(m[0,:]) == 3):
                index += 0
                index += argmin(m[0,:])
                
            if(sum(m[1,:]) == 3):
                index += 4
                index += argmin(m[1:])

            output_max[index] = 1

    m = zeros([2,4])
    for r in range(3):
        for c in range(4):
            for i in range(4):
                m[:,i] = state[:,r+3-i,c+i]

            index = 10
            if(sum(m[0,:]) == 3):
                index += 0
                index += argmin(m[0,:])
                
            if(sum(m[1,:]) == 3):
                index += 4
                index += argmin(m[1:])

            output_max[index] = 1

                                
    m = zeros([2,4])
    for r in range(3):
        for c in range(4):
            for i in range(4):
                m[:,i] = state[:,r+i,c+i]

            index = 18
            if(sum(m[0,:]) == 3):
                index += 0
                index += argmin(m[0,:])
                
            if(sum(m[1,:]) == 3):
                index += 4
                index += argmin(m[1:])

            output_max[index] = 1            
    return output_max
            
def prepare_NN_input(states):
    L = len(states)
    input_state =  zeros([L,2,6,7])
    input_2b2 = zeros([L,49,1])
    input_4b1 = zeros([L,26,1])
    
    for s_index in range(L):
        
        input_vec_2b2 = prepare_input2b2(state)
        input_vec_4b1 = prepare_input4b1(state)

        input_state = zeros([1,2,6,7])
        for i in range(2):
            for j in range(6):
                for k in range(7):
                    input_state[s_index,i,j,k] = state[i,j,k]
                    
        input_2b2 = zeros([1,49,1])
        input_4b1 = zeros([1,26,1])
        input_2b2[s_index,:,0] = input_vec_2b2
        input_4b1[s_index,:,0] = input_vec_4b1

    return [input_2b2, input_4b1, input_state]
