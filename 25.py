""" Project Euler #25: N-digit Fibonacci number """

from math import log10,floor

def digit_count(n):
    return floor(log10(n)) + 1

dp = {}
a, b = 0, 1
minValue = 0
cur = 0
i = 1
while cur < 5001:
    cur = digit_count(b)
    if cur > minValue:
        dp[cur] = i 
        minValue = cur
    i += 1
    a, b = b, a+b

for _ in range(int(input())):
    print(dp[int(input())])