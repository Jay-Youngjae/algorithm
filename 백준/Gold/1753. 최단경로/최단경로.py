
import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())

K = int(input())

links = [[] for _ in range(V+1)]
#각 노드의 값을 업데이트
dist = [1e9 for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    links[u].append([v,w]) #u에서 v로 가는 가중치w

#bfs!

q = []

heapq.heappush(q, [0, K])

dist[K] = 0


while q:
    _w, node = heapq.heappop(q)
    for nxt, weight in links[node]:
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(q, [dist[nxt], nxt])

for j in range(1, V+1):
    if dist[j] == 1e9:
        print("INF")
    else:
        print(dist[j])
