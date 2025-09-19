import sys
sys.setrecursionlimit(10**6)
def cal(alst, blst):
    asum, bsum = 0, 0
    for i in range(N//2):
        for j in range(N//2):
            asum += S[alst[i]][alst[j]]
            bsum += S[blst[i]][blst[j]]
    return abs(asum - bsum)


def dfs(idx, aidx, bidx):
    global ans
    if idx == N:
        if len(aidx) == len(bidx):
            ans = min(ans, cal(aidx, bidx))
        return
    dfs(idx + 1, aidx + [idx], bidx) # S는 애들 값 여기는 인덱스
    dfs(idx + 1, aidx, bidx + [idx])

N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]

ans = 100 * N * N
dfs(0, [], [])
print(ans)
# 트리 구조!