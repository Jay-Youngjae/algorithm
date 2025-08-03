from collections import deque
import sys
input = sys.stdin.readline

# DFS 함수 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):  # 정점 번호가 작은 것부터 방문
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 함수 정의
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):  # 정점 번호가 작은 것부터 방문
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력 받기
n, m, v = map(int, input().split())  # 노드 수, 간선 수, 시작 정점

# 그래프 초기화
graph = [[] for _ in range(n+1)]

# 간선 정보 입력받기
for _ in range(m):
    u, w = map(int, input().split())
    graph[u].append(w)
    graph[w].append(u)  # 양방향 간선

# DFS 탐색
visited = [False] * (n+1)
dfs(graph, v, visited)
print()  # 줄 바꿈

# BFS 탐색
visited = [False] * (n+1)
bfs(graph, v, visited)

