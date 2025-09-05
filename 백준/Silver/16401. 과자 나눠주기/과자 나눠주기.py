import sys
input = sys.stdin.readline
M, N = map(int, input().split()) # M명의 조카, N명의 과자

stick = list(map(int, input().split()))

# 조각의 길이를 탐색
s = 1
e = max(stick)
ans = 0


while s <= e:
    mid = (s + e) // 2
    pieces = 0
    for i in stick:
        pieces += (i // mid)
    if pieces >= M:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
print(ans)

