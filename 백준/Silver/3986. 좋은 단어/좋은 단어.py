N = int(input())
ans = 0
for _ in range(N):
    s = []
    lst = list(map(str, input().strip()))
    for l in lst:
        if len(s) == 0:
            s.append(l)
        elif s[-1] == l:
            s.pop(-1)
        else:
            s.append(l)
    if len(s) == 0:
        ans += 1

print(ans)