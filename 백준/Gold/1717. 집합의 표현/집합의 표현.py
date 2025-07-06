import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def _union(a, b): #최대높이를 확인해서 합쳐준다
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


def _find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = _find(parent[a]) #최적화
        return _find(parent[a])


n, m = map(int, input().split())
rank = [0 for _ in range(n+1)]

parent = [i for i in range(n+1)]

for _ in range(m):
    x, a, b = map(int, input().split())

    if x == 0:
        _union(a, b)
    else:
        if _find(a) == _find(b):
            print("YES")
        else:
            print("NO")