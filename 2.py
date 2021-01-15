
"""
    Fibonacci
    0 1 1 2 3 5 8 13 21 34 55 89 144
    Even :
    0 2 8 34 144 
    
    Lets try to find out relation between them 

    144 = 34 * 4 + 8
    34 = 8 * 4 + 2
    8 = 4 * 2 + 0

    So to find the next even number

    next_fib = 4 * prev_1_fib + prev_2_fib
"""
def even_fib(n):
	sum_ = 0
	prev = 0
	curr = 2
	while True:
	#	print(now_)
		if curr > n:
			return sum_
		sum_+= curr
		curr,prev = curr*4 + prev,curr
for _ in range(int(input())):
	print(even_fib(int(input())))
