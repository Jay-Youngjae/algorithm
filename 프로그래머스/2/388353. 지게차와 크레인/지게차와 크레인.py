from collections import deque
def solution(storage, requests):
    def use_lift(storage, container):
        n = len(storage)
        m = len(storage[0])
        removed = 0
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        
        queue = deque()
        visited = [[False for _ in range(m)] for _ in range(n)] 
        targets = []
        
        for y in (0, n-1):
            for x in range(m):
                if storage[y][x] == "":
                    queue.append((y,x))
                elif storage[y][x] == container:
                    targets.append((y,x))
                    removed += 1
                visited[y][x] = True
                
        for x in (0, m-1):
            for y in range(n):
                if visited[y][x] == True:
                    continue
                if storage[y][x] == "":
                    queue.append((y,x))
                elif storage[y][x] == container:
                    targets.append((y,x))
                    removed += 1
                visited[y][x] = True
                 
        while queue:
            y, x = queue.popleft()
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    continue
                elif visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                
                if storage[ny][nx] == "":
                    queue.append((ny,nx))
                elif storage[ny][nx] == container:
                    removed += 1
                    targets.append((ny, nx))
                                  
                
                
        for t in targets:
            storage[t[0]][t[1]] = ""

        
        return removed
        
    def use_crane(storage, container):
        removed = 0
        for i in range(len(storage)):
            for j in range(len(storage[0])):
                if storage[i][j] == container:
                    removed += 1
                    storage[i][j] = ""
        return removed
    
    storage = [
        list(r) for r in storage
    ]
    n = len(storage)
    m = len(storage[0])
    cnt = n * m
    
    for r in requests:
        if len(r) == 1:
            removed = use_lift(storage, r[0])
            cnt -= removed
        else:
            removed = use_crane(storage, r[0])
            cnt -= removed
    return cnt
