import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort() # 일단 정렬을 하고 A를 순회하면서 예를 들어 A가 6이라면 B에서 6이상의 원소가 처음 나오는 인덱스의 값이 cnt
    cnt = 0
    max_B = B[-1]
    len_B = len(B)
    for a in A:
        # a가 B의 최댓값보다 크면, B의 모든 원소가 a보다 작음
        if a > max_B:
            cnt += len_B
            continue

        # 인덱스를 기준으로
        s, e = 0, len_B
        while s < e:
            mid = (s + e) // 2
            if B[mid] < a:
                s = mid + 1
            else:
                e = mid
        cnt += s  #
    print(cnt)