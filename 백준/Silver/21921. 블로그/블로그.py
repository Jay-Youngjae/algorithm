import sys
input = sys.stdin.readline

N, X = map(int,input().split())

arr = list(map(int, input().split())) #1 4 2 5 1

prefix = [0 for _ in range(N+1)]
ans = []

for i in range(N):
    prefix[i+1] = prefix[i] + arr[i] #0 1 5 7 12 13


for i in range(X, N+1):
    ans.append(prefix[i]-prefix[i-X])

max_ans = max(ans)

cnt = 0
for i in range(len(ans)):
    if ans[i] == max_ans:
        cnt += 1

if set(arr) == {0}:
    print("SAD")
else:
    print(max_ans)
    print(cnt)