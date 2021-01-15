""" Project Euler #3: Largest prime factor """


def isPrime(n):
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
# print(isPrime(25))


def largest_prime_factor(n):
    if isPrime(n):
        return n
    if n % 2 == 0:
        while(n % 2 == 0):
            n //= 2
        if isPrime(n):
            return n
    p = 3
    while p*p < n:
        if n % p == 0:
            while(n % p == 0):
                #	print(n,p)
                n //= p
                if isPrime(n):
                    return n
        p += 2
    return p


for i in range(int(input())):
    print(largest_prime_factor(int(input())))
