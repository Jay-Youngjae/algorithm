import sys
input = sys.stdin.readline
N, C = map(int, input().split())

home = []
for _ in range(N):
    a = int(input())
    home.append(a)

home.sort()
start = 1
end = home[-1] - home[0]
ans = 0
while start <= end:
    distance = (start + end) // 2 # 일단 기준 거리 설정
    cnt = 1              # 첫 집에 하나 설치
    last = home[0]         # 마지막으로 설치한 집의 좌표
    for i in range(1, N):
        if home[i] - last >= distance: # 다음 집과 마지막 집간의 거리가 기준을 넘는다?
            cnt += 1
            last = home[i]

    if cnt >= C:         # 공유기 개수보다 cnt가 많다? 즉 기준이 너무 널널하다
        ans = distance
        start = distance + 1
    else:                  # 설치 불가 → 간격 줄이기
        end = distance - 1

print(ans)
'''
간격 distance를 하한선으로 잡는다 공유기들간의 최소 거리가 최대가 된다? -> 즉 모든 공유기들간의 거리가
균일하게(진짜 균일한건 아니고 가장 균형있는 상태를 추구)만들 때 비로소 최소거리가 최대가 된다.
그 기준점을 distance로 잡는다
'''