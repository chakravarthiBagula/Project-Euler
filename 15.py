""" Project Euler #15: Lattice paths """

from math import factorial as f

for _ in range(int(input())):
    n,m = map(int,input().split())
    print((f(m+n)//(f(m)*f(n)))% 1000000007)