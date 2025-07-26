import sys
input = sys.stdin.readline
N = int(input())

arr = list(map(int, input().split()))

arr = sorted(arr)

time = 0
ans = []
for i in range(N):
    time += arr[i]
    ans.append(time)


print(sum(ans))