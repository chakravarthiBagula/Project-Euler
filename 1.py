
def solve(n):
    n -= 1

    # we need to find sum of multiplies of 3 and 5
    # Best Approach -> find sum of multiples of 3
    #			   -> find sum of multiples of 5
    #               -> subtract  common multiples
    #		         15
    N3 = n // 3
    N5 = n // 5
    N15 = n // 15
    SumOf3 = (N3*(N3+1)) // 2
    SumOf5 = (N5*(N5+1)) // 2
    SumOf15 = (N15*(N15 + 1)) // 2
    res = SumOf3 * 3 + SumOf5 * 5 - SumOf15 * 15
    print(res)


for _ in range(int(input())):
    n = int(input())
    solve(n)
