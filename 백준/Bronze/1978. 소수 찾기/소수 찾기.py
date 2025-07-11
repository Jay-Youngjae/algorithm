import sys
input = sys.stdin.readline
n = int(input()) # n=4

arr = list(map(int, input().split())) # 1 3 5 7

def is_Prime_Number(x):
    if x < 2:
        return False
    #어떤 수의 int(제곱근)으로 나누어지면 소수가 아니다 -> 최적화
    for i in range(2, int(x**0.5) + 1): #소숫점 버림 , +1은 for 문 범위
        if x % i == 0:
            return False
    return True

cnt = 0
for i in arr:
    if is_Prime_Number(i) == True:
        cnt += 1
print(cnt)