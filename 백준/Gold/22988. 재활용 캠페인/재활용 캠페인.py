N, X = map(int, input().split())

arr = sorted(list(map(int,input().split())))

left = 0
right = N - 1

remain = 0
cnt = 0

while left <= right:
    s = arr[left] + arr[right]
    if arr[right] == X:
        cnt += 1
        right -= 1
        continue
    if left == right:
        remain += 1
        left += 1
        right -= 1
        continue
    if s >= X/2:
        cnt += 1
        left += 1
        right -= 1
    else:
        left += 1
        remain += 1

print(cnt + remain//3)