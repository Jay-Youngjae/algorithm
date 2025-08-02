from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 방향 벡터 (위, 아래, 왼, 오, 앞, 뒤)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()
for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == 1:
                queue.append((z,x,y))

while queue:
    z, x, y =queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and box[nz][nx][ny] == 0:
             box[nz][nx][ny] = box[z][x][y] + 1
             queue.append((nz, nx, ny))


day=0
for b in box:
    for row in b:
        if 0 in row:  # 익지 않은 토마토가 남아 있는 경우
            print(-1)
            exit()
        day = max(day, max(row))

print(day-1)