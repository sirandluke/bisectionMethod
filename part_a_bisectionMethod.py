import math
import sys

### Author: Luke Sirand

# algorithm for bisection method
# @ param a -> int storing right bound
# @ param b -> int storing left bound
# @ param itr_max -> maximum allowed iterations
# @ param tolerance -> tolerance of c
# @ return -> tuple (root,count)
def part_a_BisectionMethodAlgrthm (a,b,itr_max,tolerance):
    
    # set counter to count number of iterations
    count = 0

    # set a and b to be some arbitrary point within the interval
    a = a + 0.01
    b = b - 0.01

    # set c to an unreachable value for initialization
    c = float('inf')

    # apply algorithm until reaching tolerance or 
    # until exceeding the allowed number of iterations
    # or if tolerance is meat
    while(count < itr_max or round(tolerance,1) > abs(part_a_Func(c))):
    
        # get midpoint c
        c = (a + b) / 2
        print("midpoint is:" + str(c))

        # calculate the yCor with each xCor
        # round to nearest thousandth
        f_of_a = part_a_Func(a)
        f_of_b = part_a_Func(b)
        f_of_c = part_a_Func(c)
    
        # check if new interval is [a,c]
        if(f_of_c * f_of_a < 0):
            # set b to be the midpoint (move it right)
            b = c

        # check if new interval is [c,b]
        elif(f_of_c * f_of_b < 0):
            # set a to be the midpoint (move it left)
            a = c

        # if the comparisons are inconclusive
        else:
            # value is unreachable
            c = float('inf')
            return c,count
        # increment counter
        count = count + 1
    
    return c,count

# polynomial function for part a
# @param int cor -> xCor input 
def part_a_Func(cor):

    # try calculating with given x cor
    try: 
        #math.atan(x) takes tangent of x in radians
        f_of_x = (1/cor) - math.tan(cor)
        return f_of_x
    # if illegal operation is performed (division by zero, etc) terminate
    except:
        print("The x coordinate: " + str(cor) + " is invalid") 
        sys.exit()



# set tolerance to be 10^(-8)
tolerance = 10**-8

# Change these values if you want to try
# different intervals and change the
# iteration counter
#####################################
# maximum number of iterations
itr_max = 20

# left bound
a = 0

# right bound
b = (math.pi)/2 
#####################################

# find root with function:  x^(−1) − tan(x) 
# on interval: [0, π/2 ]
# store return value in result
result = part_a_BisectionMethodAlgrthm(a,b,itr_max,tolerance)

if (result[1] > 100 or result[0] == float("inf")):
    print("Algorithm was inconclusive")
else:
    print("The root for part a is: " + str(result[0]))
    print("At the nth iteration: " + str(result[1]))
    print("[Rounded solution: " + str(round(result[0],4)) + "]")
