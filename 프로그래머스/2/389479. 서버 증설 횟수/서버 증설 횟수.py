def solution(players, m, k):
    cnt = [0] * 24   # 각 시각별 증설된 서버 수
    answer = 0 
    active = 0 # 증설된 서버의 수

    for i in range(24):
        if i - k >= 0: # 남은 시간이 k보다 많으면
            active -= cnt[i - k] # 증설된 서버의 수 줄이기

        if players[i] == 0:
            need = 0
        else:
            need = players[i] // m
            # if (players[i] % m) != 0:  # 나머지가 있으면 서버 1대 더 필요
            #     need += 1
             
        # 부족하면 증설
        if need > active:
            extra = need - active
            cnt[i] = extra
            active += extra
        else:
            cnt[i] = 0
    print(cnt)
    
    answer = sum(cnt)

    return answer

