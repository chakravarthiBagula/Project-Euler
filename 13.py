""" Project Euler #13: Large sum """

n = int(input())
res = 0
for i in range(n):
	res += int(input())
print(str(res)[:10])