arr = list(input().strip())
for i in range(len(arr)):
    if arr[i] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        arr[i] = int(arr[i])

#for 문 이용하면 out of index 문제 때문에 while문으로 직접 관리
i = 1
while i < len(arr):
    if isinstance(arr[i-1], int) and isinstance(arr[i], int):
        arr[i] = arr[i-1] * 10 + arr[i]
        arr.pop(i-1)
    else:
        i += 1

# - 가 나오면
i = 0
curr = 0
ans = []
while i < len(arr):
    if arr[i] == '+':
        i += 1
    elif arr[i] == '-':
        ans.append(curr)
        curr = 0
        i += 1
    else:
        curr += arr[i]
        i += 1

ans.append(curr)

print(ans[0] - sum(ans[1:]))


