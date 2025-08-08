import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = []

for _ in range(N):
    arr = list(map(str, input().strip()))
    graph.append(arr)

visited = [[False for _ in range(M)] for _ in range(N)]
cnt = 0

for y in range(N):
    for x in range(M):
        if visited[y][x]:
            continue
        cnt += 1
        visited[y][x] = True

        if graph[y][x] == '-':
            nx = x + 1
            ny = y
            # 만약 아래에 같은 '-'가 있으면 이미 방문한걸로 쳐서 cnt += 1하지 않겠다
            for _ in range(M):
                if 0 <= nx < M and 0 <= ny <  N and not visited[ny][nx] and graph[ny][nx] == '-':
                    visited[ny][nx] = True
                    nx += 1


        elif graph[y][x] == '|':
            nx = x
            ny = y + 1
            # 만약 아래에 같은 'ㅣ'가 있으면 이미 방문한걸로 쳐서 cnt += 1하지 않겠다
            for _ in range(N):
                if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and graph[ny][nx] == '|':
                    visited[ny][nx] = True
                    ny += 1

print(cnt)


