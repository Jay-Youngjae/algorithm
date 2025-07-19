import sys
input = sys.stdin.readline
N = int(input())
A = set(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

for i in range(M):
    if arr[i] in A:
        print(1)
    else:
        print(0)

# M 10만(10^5) N 10만