""" Project Euler #8: Largest product in a series """

def prod(n):
	p = 1
	while n>0:
		p *= n%10
		n //= 10
	return p

t = int(input())
while (t > 0):
	N,k = map(int,input().split())
	n = input()
	max_value = 0
	for i in range(N-k+1):
		p = prod(int(n[i:i+k]))
		if p>max_value:
			max_value = p
	
	print(max_value)
	t -= 1
