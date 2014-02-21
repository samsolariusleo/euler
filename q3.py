import math

def primefactors(num):
    factor = 2
    found = False

    # find smallest factor
    while factor < num and not found:
        if num % factor == 0:
            # find the larger factor
            largest = num // factor

            # test if the number is prime
            if isprime(largest):
                 found = True
                 break
            else:
                factor = factor + 1
        else:
            factor = factor + 1
            
    return largest

def isprime(num):
    prime = True
    for i in range(2,num-1):
        if num % i == 0:
            prime = False
    return prime

print(primefactors(600851475143))
