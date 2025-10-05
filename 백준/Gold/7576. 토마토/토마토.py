from collections import deque
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0] # 북 동 남 서
dx = [0, 1, 0, -1]

queue = deque()
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 1:
            queue.append((r,c))

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0 <= nx < M and tomato[ny][nx] == 0:
            tomato[ny][nx] = tomato[y][x] + 1
            queue.append((ny, nx))

ans = 0
t = False
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            t = True
            break
        ans = max(ans, tomato[i][j])

if t == True:
    print(-1)
else:
    print((ans - 1))
