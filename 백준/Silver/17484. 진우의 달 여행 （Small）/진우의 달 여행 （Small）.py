import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

left = -1
straight = 0
right = 1
dirs = [left, straight, right]

ans = 10**9

def dfs(y, x, prev_dir, total):
    global ans
    if y == N - 1:
        ans = min(ans, total + space[y][x])
        return

    cur_sum = total + space[y][x]

    for d in dirs:
        if d == prev_dir:   # 같은 방향 연속 금지
            continue
        nx = x + d
        if 0 <= nx < M:
            dfs(y + 1, nx, d, cur_sum)


for start in range(M):
    dfs(0, start, 2, 0)

print(ans)
