def sugar(N, idx, x, y):
    min_sugar_cnt = 9999
    for i in range(N):
        for j in range(N):
            if (i * x) + (j * y) == N:
                min_sugar_cnt = min(i+j, min_sugar_cnt)

    if min_sugar_cnt == 9999:
        return -1
    else:
        return min_sugar_cnt




N = int(input())
print(sugar(N, 0, 3, 5))