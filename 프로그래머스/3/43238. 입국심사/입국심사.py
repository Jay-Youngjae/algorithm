def solution(n, times):
    start = 1
    end = min(times) * n
    ans = end
    while start <= end:
        mid = (start + end) // 2
        cnt = 0 #처리 가능한 인원
        for time in times:
            cnt += (mid // time)
        
        if cnt >= n: # 시간이 넉넉하다 ans를 갱신하고 타이트하게 당기는 시도를 한다
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans
        
    


'''
예제를 기준으로 봤을 때 찾는 최소 값은
최악의 경우 가장 빠른 한명의 입국 심사관이 모든 사람을 다 검사하는 경우 6 * 7 = 42를 상한으로 한다
즉 입국심사관을 적절히 배치해 1~42의 수 중 가장 최소가 되는 값을 찾아 출력한다.
일단 반으로 나눠서 기준점을 mid로 각 입국 심사관을 순회하며 물어본다. mid분동안 몇 명까지 심사할 수 있어? 이 값을 누적한다.
만약 n명 이상, 예제에서는 6명 이상 처리할 수 있다? mid값이 너무 크게잡혔다 -> end = mid -1로 end값 당기기
반대로 n보다 작다? 그럼 mid를 너무 작게 잡았다
'''