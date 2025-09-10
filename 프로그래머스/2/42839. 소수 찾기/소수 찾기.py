from itertools import permutations
def solution(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:  # 나누어 떨어지면 합성수
                return False
        return True
    
    n = len(numbers)
    res = set()
    cnt = 0
    for r in range(1, len(numbers) + 1):
        for p in permutations(numbers, r):
            arr = ''.join(p)
            num = int(arr)
            res.add(num)
    for i in res:
        if is_prime(i) == True:
            cnt += 1
    return cnt
