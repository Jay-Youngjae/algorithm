import sys
sys.setrecursionlimit(10**6) #재귀 제한
input = sys.stdin.readline

T = int(input())

def worm_cnt(x, y):
    if x<0 or x>=M or y<0 or y>=N: #범위 체쿠
        return 0

    if graph[y][x] == 0:
        return 0

    #위의 조건식에 걸리지 않았다면
    graph[y][x] = 0 #사실상 visited[y][x] = True 즉 방문처리

    worm_cnt(x-1,y)
    worm_cnt(x+1,y)
    worm_cnt(x,y-1)
    worm_cnt(x,y+1)

    return 1
for _ in range(T):
    M, N, K = map(int, input().split())

    X, Y = [], []

    for _ in range(K):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)


    graph =[[0 for _ in range(M)] for _ in range(N)]

    for i in range(K):
        graph[Y[i]][X[i]] = 1

    cnt = 0
    for x in range(M):
        for y in range(N):
            if worm_cnt(x, y) != 0:
                cnt += 1

    print(cnt)