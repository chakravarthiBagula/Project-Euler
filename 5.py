""" Project Euler #5: Smallest multiple """

import math

def lcm(a,b):
	return (a*b)//(math.gcd(a,b))
t = int(input())

while (t > 0):
	n = int(input())
	result = 1
	for i in range(1,n+1):
		result = lcm(result,i)
	print(result)
	t -= 1