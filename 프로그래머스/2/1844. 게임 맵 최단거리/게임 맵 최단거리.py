from collections import deque
def solution(maps):

    n = len(maps) #열 
    m = len(maps[0]) #행
    
    
    def bfs(maps, n, m):
        dy = [-1, 0, 1, 0] # 북 동 남 서
        dx = [0, 1, 0, -1]
        queue = deque([(0, 0)])
        maps[0][0] = 1
        while queue:
            y, x = queue.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=ny<n and 0<=nx<m and maps[ny][nx] == 1: #어차피 방문했다면 값이 2, 3, 4 등등일테니 1이라는 것은 길이면서 방문하지 않았다는 뜻
                    maps[ny][nx] = maps[y][x] + 1 
                    queue.append((ny, nx))
        if maps[n-1][m-1] == 1:
            return -1
        else:
            return maps[n-1][m-1]
                
    answer = bfs(maps, n, m)
    return answer