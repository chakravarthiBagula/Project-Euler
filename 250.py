""" Project Euler #230: Fibonacci Words """
def FibWords(A, B, n):
    n = int(n)
    if n <= len(A):
        print(A[n - 1])
        return
    if n <= len(B):
        print(B[n - 1])
        return
    seq = [len(A), len(B)]
    idx = 1
    while seq[idx] < n:
        idx += 1
        seq.append(seq[-1]+seq[-2])
    
    while idx > 1:
        if n > seq[idx - 2]:
            n -= seq[idx - 2]
        else:
            idx -= 1
        idx -= 1
    if idx == 1:
        print(B[n-1])
    else:
        print(A[n-1])

for _ in range(int(input())):
    FibWords(*(input().split()))
