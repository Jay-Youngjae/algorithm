# 왼쪽 괄호 개수만 카운트 어차피 오른쪽 카운트가 많아지는 순간 vps 성립 불가
# 즉 cnt == 0 일때 yes
def VPS(lst):
    cnt = 0
    for i in lst:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0: #오른쪽이 더 많아지는 경우 / 오른쪽이 먼저 들어온 경우
            return "NO"
    if cnt == 0:
        return "YES"
    else:
        return "NO"


T = int(input())


for _ in range(T):
    lst = list(input())
    print(VPS(lst))
