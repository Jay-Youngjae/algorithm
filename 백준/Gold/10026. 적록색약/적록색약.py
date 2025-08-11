from collections import deque
import copy, sys
input = sys.stdin.readline
def picture(graph, visited, y, x):
    queue = deque([(y,x)])
    visited[y][x] = True
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N:
                if graph[y][x] == graph[ny][nx] and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
    return 1


N = int(input())
graph = [list(map(str, input().strip())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
color_weakness_visited = copy.deepcopy(visited)
color_weakness_graph = copy.deepcopy(graph) # 처음엔 그냥 graph를 대입했으나 이러면 얕은복사로 주소값이 공유돼 기존 graph도 RG로 변해버림
for i in range(N):
    for j in range(N):
        if color_weakness_graph[i][j] == 'R' or color_weakness_graph[i][j] == 'G':
            color_weakness_graph[i][j] = 'RG'

picture_cnt = 0
color_weakness_picture_cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            picture_cnt += picture(graph, visited, i, j)


for i in range(N):
    for j in range(N):
         if not color_weakness_visited[i][j]:
            color_weakness_picture_cnt += picture(color_weakness_graph, color_weakness_visited, i, j)

print(picture_cnt, end = ' ')
print(color_weakness_picture_cnt)

# 2583이랑 좀 비슷한 느낌 덕분에 쉽게 풀었다