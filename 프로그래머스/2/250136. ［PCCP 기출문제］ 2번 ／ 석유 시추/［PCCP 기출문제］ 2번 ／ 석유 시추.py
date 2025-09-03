import sys
sys.setrecursionlimit(10**6)

def solution(land): # 1이면 석유 있음 0은 그냥 땅
    def oil_cnt(y, x):
        dy = [-1, 0, 1, 0] # 북 동 남 서 
        dx = [0, 1, 0, -1]
        visited[y][x] = True
        cols.add(x)
        cnt = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<m and 0<=ny<n and land[ny][nx] == 1 and not visited[ny][nx]:
                cnt += oil_cnt(ny, nx)
                
        return cnt
    
    
    n = len(land)
    m = len(land[0])
    ans = [0] * m
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                cols = set()
                size = oil_cnt(i, j)
                for c in cols:
                    ans[c] += size

    return max(ans)