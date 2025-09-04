import sys
input = sys.stdin.readline

def calc_max_min(idx, cur, add, sub, mul, div):
    # 모든 숫자를 다 썼다면 현재 값이 최댓값이자 최솟값
    if idx == N:
        return cur, cur

    x = arr[idx]
    cand_max = -10**18
    cand_min =  10**18

    if add > 0:
        mx, mn = calc_max_min(idx + 1, cur + x, add - 1, sub, mul, div)
        cand_max = max(cand_max, mx)
        cand_min = min(cand_min, mn)

    if sub > 0:
        mx, mn = calc_max_min(idx + 1, cur - x, add, sub - 1, mul, div)
        cand_max = max(cand_max, mx)
        cand_min = min(cand_min, mn)

    if mul > 0:
        mx, mn = calc_max_min(idx + 1, cur * x, add, sub, mul - 1, div)
        cand_max = max(cand_max, mx)
        cand_min = min(cand_min, mn)

    if div > 0:
        nx = int(cur / x)
        mx, mn = calc_max_min(idx + 1, nx, add, sub, mul, div - 1)
        cand_max = max(cand_max, mx)
        cand_min = min(cand_min, mn)

    return cand_max, cand_min

N = int(input().strip())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())


max_ans, min_ans = calc_max_min(1, arr[0], add, sub, mul, div)
print(max_ans, min_ans)
