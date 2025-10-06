def solution(land):
    for i in range(1, len(land)):
        a, b, c, d = land[i-1]  # 바로 위 행 4칸
        land[i][0] += max(b, c, d)  # 같은 열(0)은 제외
        land[i][1] += max(a, c, d)
        land[i][2] += max(a, b, d)
        land[i][3] += max(a, b, c)
    return max(land[-1])
