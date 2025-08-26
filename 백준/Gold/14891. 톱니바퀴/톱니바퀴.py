from collections import deque

wheels = [deque(map(int, input().strip())) for _ in range(4)]

K = int(input().strip())
for _ in range(K):
    n, d = map(int, input().split())
    n -= 1

    # 1~4번 톱니의 회전 방향: 0(안돈다), 1(시계), -1(반시계)
    direaction = [0, 0, 0, 0]
    direaction[n] = d

    # 왼쪽으로 전파 (맞닿는 극이 다르면 반대로 회전)
    j = n
    while j - 1 >= 0: # 예를 들어 3번 톱니바퀴라면 n=2 j=2인 상태 -> 예제 상에선 j를 줄이면서 왼쪽을 탐색해도 회전x
        if wheels[j][6] != wheels[j-1][2]:
            direaction[j - 1] = -direaction[j] #반대로
        else:
            break
        j -= 1

    # 오른쪽으로 전파
    j = n
    while j + 1 <= 3: # 예를 들어 3번 톱니바퀴라면 n=2 j=2인 상태 -> 예제 상에선 j를 줄이면서 오른쪽을 탐색하면
                      # 4번 톱니바퀴랑 달라서 여기서 4번 톱니바퀴의 회전이 일어난다
        if wheels[j][2] != wheels[j+1][6]:
            direaction[j + 1] = -direaction[j]
        else:
            break
        j += 1

    for i in range(4): # 앞선 반복문에서 각 톱니바퀴의 회전 방향을 정해놓은 것을 여기서 적용
        if direaction[i] == 1:         # 시계
            x = wheels[i].pop()
            wheels[i].appendleft(x)
        elif direaction[i] == -1:      # 반시계
            x = wheels[i].popleft()
            wheels[i].append(x)

# 점수 계산
ans = wheels[0][0] + wheels[1][0]*2 + wheels[2][0]*4 + wheels[3][0]*8
print(ans)
