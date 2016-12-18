
from numpy import *


def test():
    x = linspace(0,10,11)

    print 'test ',x[4:6]

    m = zeros([2,2,2])
    m[1,0,0] = 4
    m[0,1,1] = 1

    print sum(m)
    print amax(m)
    

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
    
