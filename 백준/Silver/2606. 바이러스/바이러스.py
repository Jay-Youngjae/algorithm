from collections import deque
import sys
si = sys.stdin.readline

def bfs(graph, start, visited, component):
    queue=deque([start])
    visited[start]=True
    component.append(start)
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                component.append(i)


n = int(si())  # 컴퓨터의 수 (노드 수)
m = int(si())  # 연결된 컴퓨터의 쌍 (간선 수)

graph=[[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, si().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프이므로 양쪽에 간선 추가
visited=[False]*(n+1)

component_1 = []  # 노드 1과 연결된 컴포넌트를 저장할 리스트

bfs(graph, 1, visited, component_1)

print(len(component_1)-1)

