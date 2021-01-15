""" Project Euler #16: Power digit sum   """
from math import log10, floor
def sum_of_digits(n):
    return floor(log10(n)) + 1
def private_sum(n):
    return sum_of_digits(2**n)
for i in range(int(input())):
    print(private_sum(int(input())))
