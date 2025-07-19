N = int(input())
lst = []

for _ in range(N):
    s = input().split()
    lst.append(s)



arr = []
for i in range(N):
    if lst[i][0] == "push":
        arr.append(lst[i][1])
    elif lst[i][0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif lst[i][0] == "size":
        print(len(arr))
    elif lst[i][0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif lst[i][0] == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])