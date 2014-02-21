import math

def primefactors(num):

    # define variables
    primes = []
    primefactors = []
    
    # generate list of prime numbers
    for i in range(2, num):
        if isprime(i):
            primes.append(i)
    
    # from primes, test if they are factors
    for prime in primes:
        if num % prime == 0:
            primefactors.append(prime)

    # return largest prime number
    return primefactors[-1]

def isprime(num):
    prime = True
    for i in range(2,num-1):
        if num % i == 0:
            prime = False
    return prime

print(primefactors(600851475143))
