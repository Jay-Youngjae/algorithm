from collections import deque
N = int(input())

arr = []
for _ in range(N):
    a = input().split()
    arr.append(a)

q = deque()

for i in range(N):
    if arr[i][0] == "push":
        q.append(arr[i][1])

    elif arr[i][0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            p = q.popleft()
            print(p)

    elif arr[i][0] == "size":
        print(len(q))

    elif arr[i][0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif arr[i][0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif arr[i][0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])


