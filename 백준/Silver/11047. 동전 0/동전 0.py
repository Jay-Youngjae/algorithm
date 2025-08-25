N, K = map(int, input().split())

Ai = []
for _ in range(N):
    a = int(input())
    Ai.append(a)

cnt = 0
for i in range(N-1, -1, -1):
    cnt += K // Ai[i]
    K = K % Ai[i]

print(cnt)