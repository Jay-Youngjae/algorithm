N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]
ans = []
p = K-1
while lst:
    if p >= len(lst):
        p %= len(lst)
    t = lst.pop(p)
    ans.append(t)
    p += K - 1 # 하나가 pop되어서

print("<" + ", ".join(map(str, ans)) + ">")
