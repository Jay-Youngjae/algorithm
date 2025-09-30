N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort()

ans = 0
for i in range(N):            # i번째가 최소면 사용 개수는 N-i
    ans = max(ans, ropes[i] * (N - i))

print(ans)
