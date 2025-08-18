from collections import deque

def min_time(n, w, L, weight):
    time = 0
    idx = 0
    sum_weight = 0
    queue = deque([0] * w)

    while idx < n or sum_weight > 0:
        time += 1
        sum_weight -= queue.popleft()
        # 다음 트럭을 올릴 수 있으면 올림, 아니면 빈칸
        if idx < n and sum_weight + weight[idx] <= L:
            queue.append(weight[idx])
            sum_weight += weight[idx]
            idx += 1
        else: #그냥 append하고 pop하고 난리였는데 깔끔하게 0을 올리면 된다!
            queue.append(0)

    return time

n, w, L = map(int, input().split())
#트럭 수, 다리 길이, 다리 최대 하중
weight = list(map(int, input().split()))
print(min_time(n, w, L, weight))
