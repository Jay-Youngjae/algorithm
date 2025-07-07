import sys
from itertools import combinations
input = sys.stdin.readline

def cal(lst):
    min_sum = 0
    for hi, hj in home:
        _min = 2 * N
        for ci, cj in lst:
            _min = min(_min, abs(hi - ci) + abs(hj - cj))
        min_sum += _min
    return min_sum

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

ans = 2 * 2 * N * N


for comb in combinations(chicken, M):
    ans = min(ans, cal(comb))

print(ans)
