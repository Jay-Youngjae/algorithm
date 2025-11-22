
def solution(cards):
    cycles = []
    n = len(cards)
    visited = [False for _ in range(n)]
    
    def search(j, l):
        if visited[j]:
            cycles.append(l) # l = 사이클의 크기
            return
        visited[j] = True
        nxt = cards[j] -1 # nxt 다음 탐색 지점
        search(nxt, l+1)
        
    for i in range(n):
        if visited[i]:
            continue
        search(i, 0)
    
    print(cycles)
    if len(cycles) < 2:
        return 0
    cycles.sort(reverse = True)
    return cycles[0] * cycles[1]

