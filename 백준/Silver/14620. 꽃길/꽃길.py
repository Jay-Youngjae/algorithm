import sys
input = sys.stdin.readline

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 각 위치의 꽃 한 송이 비용 미리 계산
price = [[0]*N for _ in range(N)]
for i in range(1, N-1):
    for j in range(1, N-1):
        s = field[i][j]
        for k in range(4):
            s += field[i+dy[k]][j+dx[k]]
        price[i][j] = s

visited = [[False]*N for _ in range(N)]
centers = [(i, j) for i in range(1, N-1) for j in range(1, N-1)]
ans = float('inf')


def can_place(y, x):
    if visited[y][x]:
        return False
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if visited[ny][nx]:
            return False
    return True


def dfs(idx, picked, total):
    global ans
    if picked == 3:
        ans = min(ans, total)
        return
    if total >= ans:  # 가지치기
        return
    if idx == len(centers):
        return

    y, x = centers[idx]

    # 꽃을 심는 경우
    if can_place(y, x):
        # 방문 표시 (중앙 + 상하좌우)
        visited[y][x] = True
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            visited[ny][nx] = True

        dfs(idx + 1, picked + 1, total + price[y][x])

        # 방문 해제 (백트래킹)
        visited[y][x] = False
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            visited[ny][nx] = False

    # 꽃을 심지 않는 경우
    dfs(idx + 1, picked, total)


dfs(0, 0, 0)
print(ans)
