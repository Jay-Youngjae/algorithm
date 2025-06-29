N, M = map(int, input().split())
forest = list(map(int, input().split()))

left = 1
right = max(forest)

while left <= right:
    mid = (left+right)//2
    wood = 0
    for tree in forest:
        if tree > mid:
            wood += tree - mid
    if wood >= M:
        left = mid + 1
    else:
        right = mid - 1
print(right)