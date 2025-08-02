from collections import deque

n, m = map(int, input().split())

maze=[list(map(int, input())) for _ in range(n)]


def bfs(maze, n, m):
    # 북 동 남 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue=deque([(0,0)])
    maze[0][0]=1
    while queue:
        x, y= queue.popleft()
        if x==n-1 and y==m-1:
            return maze[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                # 이동한 칸에 현재까지의 칸 수를 기록하고 큐에 삽입
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))


result=bfs(maze, n, m)
print(result)