from collections import Counter 
def solution(participant, completion):
    
    p = Counter(participant)
    c = Counter(completion)
    ans = list((p - c).keys())
    answer = ans[0]
    return answer
    