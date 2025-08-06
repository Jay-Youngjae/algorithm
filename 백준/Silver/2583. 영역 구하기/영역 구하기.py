from collections import deque
import sys
input = sys.stdin.readline
M, N, K = map(int, input().split())

def bfs(x, y, graph, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    queue.append((nx, ny))
    return cnt


graph = [[0 for _ in range(N)] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

ans = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and not visited[i][j]:
            ans.append(bfs(i, j, graph, visited))


ans.sort()
print(len(ans))
print(*ans)



