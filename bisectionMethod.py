def bMethodAlgrthm (a,b,coef,tolerance):
    
    # initialize c to a random unreachable value
    c = float(100)
    count = 0
    while(polyFunc(c,coef) > tolerance):
        c = (a + b) / 2

        if(polyFunc(a,coef) * polyFunc(c,coef) < 0):
            b = c
            print("c" + str(count) + " is: " + str(c))
            count = count + 1
        elif(polyFunc(b,coef) * polyFunc(c,coef) < 0):
            a = c
            print("c" + str(count) + " is: " + str(c))
            count = count + 1
        else:
            #algorithm is inconclusive
            return
    return c





def generatePoly(arr):
    res = ""
    power = 2
    for i in arr:
        if power == 0:
            res = res + str(i)
        else :
            res = res + str(i) + 'x' + '^' + str(power) + " + "
            power = power - 1
    return res

def polyFunc(xCor,arr):
    ans = 0
    power = 2
    for i in arr:
        ans = ans + int(i)*(xCor**power)
        power = power - 1
    return ans



# ask for user input
n = input("input three numbers sepereated by spaces: ")

# split array at the spaces
coef = list(n.split(' '))

# pass in array to give mathematical expression of input
expression = generatePoly(coef)

aCor = input("Enter the initial lower bound x coordinate: ")
bCor = input("Enter the initial upper bound x coordinate: ")
abRange = '[' + str(aCor) + ',' + str(bCor) + ']'
aCor = int(aCor)
bCor = int(bCor)

tolerance = input("Enter tolerance n [10^n]: ")
tolerance = 10**int(tolerance)


print("The expression you entered is:" + expression)
print("On the Domain: " + abRange)
print("And with tolerance: " + str(tolerance))

root = bMethodAlgrthm(aCor,bCor,coef,tolerance)

print("The root value at tolerance " + str(tolerance) + " is:" )
print(root)




