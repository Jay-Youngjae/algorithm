import sys
sys.stdin.readline

#1. 모든 링크를 한번에 가져온다
#2. 링크를 연결 하면서 같은 집합으로 만든다
#3. 이미 같은 집합이라면 연결하지 않는다

def _find(x):
    while parent[x] !=x:
        x = parent[x]
    return x

def _union(a, b):
    a = _find(a)
    b = _find(b)
    if a == b:
        return
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        rank[b] += 1

V, E = map(int, input().split())

link = [list(map(int, input().split())) for _ in range(E)]

link.sort(key=lambda x:x[2]) #3번째 값인 가중치를 기준으로 정렬

parent = [i for i in range(10**6)]
rank = [0 for _ in range(10**6)] #노드의 깊이

ans = 0

for i in range(E):
    A = link[i][0]
    B = link[i][1]
    W = link[i][2]

    A = _find(A)
    B = _find(B)

    if A==B:
        continue
    else:
        _union(A,B)
        ans += W

print(ans)