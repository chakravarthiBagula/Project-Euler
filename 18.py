""" Project Euler #18: Maximum path sum I """

def solve():
    n = int(input())
    tri = [list(map(int, input().split())) for _ in range(n)][::-1]
    idx, temp = 1, n - 1
    while idx < n:
        k = 0
        while k < temp:
            tri[idx][k] += max(tri[idx-1][k:k+2])
            k += 1
        temp -= 1
        idx += 1
    print(tri[n-1][0])
    
    
k = int(input())
while k:
    solve()
    k -= 1