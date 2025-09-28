from itertools import combinations

def solution(n, q, ans):
    answer = 0
    m = len(ans)
    total = list(combinations(range(1, n+1), 5))
    for t in total:
        for i in range(m):
            cnt = 0
            for j in q[i]:
                if j in t:
                    cnt += 1
            if cnt != ans[i]:
                break
        else:
            answer += 1
    return answer


'''
전체 경우의 수 = total
for 문을 통해 경우의 수를 전체 경우의 수와 비교
일치하면 ans += 1


'''