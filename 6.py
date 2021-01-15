""" Project Euler #6: Sum square difference """

t = int(input())
while (t > 0):
	n = int(input())
	result = (n*(n+1)*(3* n * n - n -2))//12
	print(result)
	t -= 1

