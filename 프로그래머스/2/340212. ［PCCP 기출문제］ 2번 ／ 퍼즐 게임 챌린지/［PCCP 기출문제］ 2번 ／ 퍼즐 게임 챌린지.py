def solution(diffs, times, limit):
    n = len(diffs)
    def calc(level):
        total = 0
        time_prev = 0
        for i in range(n):
            if diffs[i] <= level:
                total += times[i]
            else:
                total += (times[i] + time_prev) * (diffs[i] - level) + times[i]
            time_prev = times[i]
        return total
                
    start = 1
    end = max(diffs)
    while start <= end:
        mid = (start + end) // 2
        if calc(mid) <= limit:
            end = mid - 1
        else:
            start = mid + 1
            
        
    #이분탐색으로 접근-> a값의 증가/감소에 따라 b값의 증가/감소 + 증/감이 단방향으로 움직임
    return start
