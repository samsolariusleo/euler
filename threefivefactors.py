def threefivefactors(limit):
    # define variables
    multiples = []

    # initialize the first prime number
    num = 3
    while num < limit:
        if num % 3 == 0 or num % 5 == 0:
            multiples.append(num)
        num = num + 1
    return multiples

print(threefivefactors(1000))
        
