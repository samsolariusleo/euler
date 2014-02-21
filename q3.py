import math

def primefactors(num):
    primelimit = "{0:.0f}".format(math.sqrt(num))
    primelimit = int(primelimit)
    factor = 2
    found = False

    # find smallest factor
    while factor < primelimit and not found:
        if num % factor == 0:
            # find the larger factor
            largest = num // factor
            
            # test if the number is prime
            if isprime(largest):
                found = True
                return largest
            else:
                factor = factor + 1
        else:
            factor = factor + 1
    return "Not found."

def isprime(num):
    primelimit = "{0:.0f}".format(math.sqrt(num))
    primelimit = int(primelimit)
    
    prime = True
    for i in range(2,primelimit):
        if num % i == 0:
            prime = False
    return prime

print(primefactors(13195))
print(primefactors(600851475143))
