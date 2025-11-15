import sys
input = sys.stdin.readline

def shortest_len():
    min_len = float('inf')

    for idxs in positions:
        if len(idxs) < K:
            continue

        # K개씩 묶어서 최소 길이 찾기
        for i in range(len(idxs) - K + 1):
            length = idxs[i + K - 1] - idxs[i] + 1
            if length < min_len:
                min_len = length

    return min_len if min_len != float('inf') else -1


def longest_len():
    max_len = 0

    for idxs in positions:
        if len(idxs) < K:
            continue

        # K개씩 묶어서 최대 길이 찾기
        for i in range(len(idxs) - K + 1):
            length = idxs[i + K - 1] - idxs[i] + 1
            if length > max_len:
                max_len = length

    return max_len if max_len != 0 else -1


T = int(input())
for _ in range(T):
    W = list(input())
    K = int(input())

    # 각 알파벳(a~z)의 등장 위치를 저장할 리스트
    positions = [[] for _ in range(26)]
    for i, ch in enumerate(W):
        idx = ord(ch) - ord('a')
        if 0 <= idx < 26:
            positions[idx].append(i)

    ans1 = shortest_len()
    ans2 = longest_len()

    if ans1 == -1:
        print(-1)
    else:
        print(ans1, ans2)
