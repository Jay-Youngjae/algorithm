import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def ATOB(idx, A, B):
    if A == B:
        return idx
    if A > B:
        return float('inf')
    ans = min(ATOB(idx+1, A * 2, B), ATOB(idx+1, A * 10 + 1, B))
    return ans

A, B = map(int, input().split())

result = ATOB(1, A, B)
if result >= float('inf'):
    print(-1)
else:
    print(result)