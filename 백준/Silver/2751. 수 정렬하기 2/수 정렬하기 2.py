import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst = sorted(lst)
for i in range(N):
    print(lst[i])