""" Project Euler #9: Special Pythagorean triplet """
def pythogorian(N):
   max_p = -1
   for a in range(1,N//3 +1):
   	b = (N*N - 2 * a * N)//(2*(N-a))
   	c = (N-a-b)
   	if a*a + b*b == c*c :
   		p = a * b * c
   		if p > max_p:
   			max_p = p
   print(max_p)
			
t = int(input())
while t > 0:
	pythogorian(int(input()))
	t -= 1
