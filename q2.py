def genfibonaccis(limit):
    # define variables
    fibonnacis = []

    # initialize the first number    
    firstnum = 1
    nextnum = 2

    # generate fibonacci
    while firstnum < limit:
        # find the fibonacci number
        fibonnacis.append(firstnum + nextnum)
        firstnum = nextnum
        nextnum = fibonnacis[-1]
    return fibonnacis

def findevensum(array):
    # initialize variables
    total = 0

    # add each number to total if it is even
    for item in array:
        if item % 2 == 0:
            total = total + item

    return total

print(findevensum(genfibonaccis(4000000)))
