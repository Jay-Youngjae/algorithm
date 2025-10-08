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

"""
일단 요청이 들어왔는데 하나짜리 요청이다!
그럼 storage[0][0~m], storage[0~n][0], storage[n][0~m], storage[0~n][m]에 해당하는 글자를 제거한다

두개짜리 요청이다! -> 해당 글자를 전부 제거한다

여기서 문제는 한번 제거한 이후 바깥에 해당하는 글자만 어떻게 깔끔하게 제거할것인가
그럼 비어있는 공간에 임의의 문자 '0'을 넣는건 어떨까
그래서 if storage == '0'이라면 i+1 을 대입시키는거지
"""