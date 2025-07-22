import heapq, sys
input = sys.stdin.readline
N = int(input())

hq = []
max_day = 0

# 과제 입력 및 최대 힙 구성
for _ in range(N):
    d, w = map(int, input().split())
    heapq.heappush(hq, (-w, d))
    max_day = max(max_day, d)

# 각 날짜에 과제 했는지 체크할 배열
day_check = [False] * (max_day + 1)

score = 0

while hq:
    w, d = heapq.heappop(hq)
    w = -w  # 다시 양수로

    # 가능한 날짜 중 가장 늦은 날부터 찾아서 배정
    for day in range(d, 0, -1):
        if not day_check[day]:
            day_check[day] = True
            score += w
            break  # 과제 하나만 할 수 있음

print(score)
