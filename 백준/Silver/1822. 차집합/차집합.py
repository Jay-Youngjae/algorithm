na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
ans = a - b

print(len(ans))
print(*sorted(ans))