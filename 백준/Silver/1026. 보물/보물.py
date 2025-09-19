import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = [0] * N

A = sorted(A, reverse = True)
B.sort()
for i in range(N):
    S[i] = A[i] * B[i]

sum_s = sum(S)
print(sum_s)

