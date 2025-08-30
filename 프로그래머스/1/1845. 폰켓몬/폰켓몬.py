import math
def solution(nums):
    n = len(set(nums))
    m  = len(nums)//2
    answer = 0
    if n > m:
        answer = m
    else:
        answer = n
                
    return answer