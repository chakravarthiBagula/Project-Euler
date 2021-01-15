""" Project Euler #10: Summation of primes """

up = 1000000

prime = [False,False] + [True]*(up-2)

sumUp = [0]*up

for i,p in enumerate(prime):
	if p:
		sumUp[i] = sumUp[i-1] + i
		for it in range(i*i,up,i):
			prime[it] = False
	else:
		sumUp[i] = sumUp[i-1]

t = int(input())

for i in range(t):
	n = int(input())
	print(sumUp[n])