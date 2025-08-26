import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 끝나는 시간, 시작 시간 기준 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
last_end = 0
for start, end in meetings:
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)