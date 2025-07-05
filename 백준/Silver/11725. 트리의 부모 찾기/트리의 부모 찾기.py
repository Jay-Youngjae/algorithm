import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]


for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def recur(node, pre): #pre는 이전 노드

    parent[node] = pre

    for nxt in graph[node]:
        if nxt == pre:
            continue
        recur(nxt, node)

recur(1, 0)

for i in range(2, N+1):
    print(parent[i])