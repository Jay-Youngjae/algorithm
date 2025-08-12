def solution(info, edges): #info = 양/늑대 정보 배열 0은양 1은늑대 , edges = 부모/자식 관계 info의 길이상 재귀
    n = len(info)
    graph = [[] for _ in range(n)]
    for p, c in edges:
        graph[p].append(c)
    visited = [False] * n
             
    def dfs(idx, sheep_cnt, wolf_cnt):
        
        if info[idx] == 0 and not visited[idx]:
             sheep_cnt += 1
        elif info[idx] == 1 and not visited[idx]:
             wolf_cnt += 1
        visited[idx] = True
        if sheep_cnt <= wolf_cnt:
             visited[idx] = False
             return 0
        max_sheep_cnt = sheep_cnt
        for i in range(n):
             if visited[i]:
                 for child in graph[i]:
                     if not visited[child]:
                         max_sheep_cnt = max(max_sheep_cnt, dfs(child, sheep_cnt, wolf_cnt))
        visited[idx] = False
        return max_sheep_cnt
        

    answer = dfs(0,0,0)
    return answer