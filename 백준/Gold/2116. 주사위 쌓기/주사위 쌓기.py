def side_max(dice, bottom_idx, top_idx):
    # 아랫면, 윗면 제외한 4면의 최댓값
    m = 0
    for i, v in enumerate(dice):
        if i == bottom_idx or i == top_idx:
            continue
        if v > m:
            m = v
    return m

N = int(input())

dice = [list(map(int, input().split())) for _ in range(N)]

mapping = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

answer = 0

# 첫 주사위의 '아랫면 인덱스'를 0~5로 시도
for first_bottom in range(6):
    total = 0
    bottom_idx = first_bottom
    top_idx = mapping[bottom_idx] #예를 들어 처음 0 -> 5
    # 첫 주사위의 윗면 숫자
    top_num = dice[0][top_idx]
    total += side_max(dice[0], bottom_idx, top_idx)

    # 2번째 주사위부터 위로 쌓기
    for i in range(1, N):
        # 현재 주사위에서 아랫 주사위의 윗면(top_num)과 같은 숫자를 가진 인덱스를 찾음
        bottom_idx = dice[i].index(top_num)   # 6면뿐이라 O(6) 탐색 가능
        top_idx = mapping[bottom_idx]
        top_num = dice[i][top_idx]
        total += side_max(dice[i], bottom_idx, top_idx)

    if total > answer:
        answer = total

print(answer)