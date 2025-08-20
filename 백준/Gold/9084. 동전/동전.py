T = int(input())
for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M+1)
    dp[0] = 1 #0원은 아무 동전도 쓰지 않는 경우의 수 단 1개
    # 경우의 수 누적
    for i in coin:
        for j in range(i, M+1): #1부터 1000까지
            dp[j] += dp[j - i] # 각 인덱스에 for문을 돌면서 경우의 수를 지속적으로 누적한다
                               

    print(dp[M])
