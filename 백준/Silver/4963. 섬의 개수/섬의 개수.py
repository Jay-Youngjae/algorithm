import sys
sys.setrecursionlimit(10**6)
def dfs(y, x):
    if graph[y][x] == 0:
        return
    visited[y][x] = True
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < h and 0 <= nx < w:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(ny, nx)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]

    dy = [-1, 0, 1, 0, -1, -1, 1, 1]
    dx = [0, 1, 0, -1, -1, 1, -1, 1]


    ans = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                ans += 1

    print(ans)