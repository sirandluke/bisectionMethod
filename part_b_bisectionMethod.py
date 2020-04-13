import math
import sys

# algorithm for bisection method
# @ param a -> int storing right bound
# @ param b -> int storing left bound
# @ param itr_max -> maximum allowed iterations
# @ param tolerance -> tolerance of c
# @ return -> tuple (root,count)
def part_b_BisectionMethodAlgrthm (a,b,itr_max,tolerance):
    
    # set counter to count number of iterations
    count = 0

    # set c to an unreachable value for intialization
    c = float('inf')
    # apply algoirthm until reaching tolerance or 
    # until exceeding the allowed number of iterations
    while(part_b_Func(c) > tolerance or count < itr_max):
    
        # get midpoint c
        c = (a + b) / 2
        
        print("midpoint is:" + str(c))

        # calculate the yCor with each xCor
        # round to nearest thousandth
        f_of_a = part_b_Func(a)
        f_of_b = part_b_Func(b)
        f_of_c = part_b_Func(c)

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

# polynomial function for part b
# @param int cor -> xCor input 
def part_b_Func(cor):

    # try calculating with given x cor
    try: 
        #math.atan(x) takes tangent of x in radians
        f_of_x = (1/cor) - 2**cor
        return f_of_x
    # if illegal operation is performed (divison by zero, etc) terminate
    # program
    except:
        print("The x coordinate: " + str(cor) + " is invalid") 
        sys.exit()



# set tolerance to be 10^(-8)
tolerance = 10**(-8)

# define maximum number of iterations
itr_max = 2

# find root with funcnction:  x^(−1) − 2^(x) 
# on interval: [0, 1]
# store return value in result
result = part_b_BisectionMethodAlgrthm(0,(math.pi)/2,itr_max,tolerance)

if (result[1] > 100 or result[0] == float("inf")):
    print("Algorithm was inconclusive")
else:
    print("The root is: " + str(result[0]))
    print("At the nth iteration: " + str(result[1]))
