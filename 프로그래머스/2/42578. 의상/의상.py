def solution(clothes):
    kinds = []
    for c in clothes:
        kinds.append(c[1])  
    set_kinds = list(set(kinds))
    cnts= []
    for s in set_kinds:
        cnt = 0
        for c in clothes:
            if c[1] == s:
                cnt += 1
        cnts.append(cnt)
    answer = 1
    for c in cnts:
        answer *= (c + 1)
    return answer - 1 #아무것도 안입는 경우

#각 종류는 {a, b}라고 했을 때 안입는 경우, a를 입는 경우, b를 입는경우 총 3개로 나눠질수 있다.
