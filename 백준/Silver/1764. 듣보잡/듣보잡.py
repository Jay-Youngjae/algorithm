N, M = map(int, input().split())

d = set()
b = set()

for _ in range(N):
    t = input()
    d.add(t)

for _ in range(M):
    t = input()
    b.add(t)

ans = d & b

print(len(ans))
ans = sorted(ans)
for a in ans:
    print(a)

