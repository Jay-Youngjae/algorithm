import sys
input = sys.stdin.readline

#최대 M개를 고른다 즉 M개 미만으로 남기는 것도 가능하다!
def cal(lst):
    #모든 집과 해당 치킨집의 거리중 최소값을 구해 누적
    min_sum = 0
    for hi, hj in home:
        _min = 2 * N
        for ci, cj in lst:
            _min = min(_min, abs(hi-ci)+abs(hj-cj))
        min_sum += _min
    return min_sum

def dfs(n, lst):
    global ans
    if n == cnt:
        if len(lst) == M:
            ans = min(ans, cal(lst))
        return
    dfs(n+1, lst+[chicken[n]]) # 치킨집 유지
    dfs(n+1, lst) # 폐업


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dist = 0
home = []
chicken = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

cnt = len(chicken)

ans = 2*2*N*N

dfs(0, []) #n은 치킨집 번호(개수)

print(ans)