def solution(n, w, num): # n: 택배 개수, w: 가로 개수, num: 꺼내려는 택배 상자 번호 
    col = (num - 1) % w # 전체 층의 수 인덱스
    interval_Q = (n - num) // (2 * w)  # 2칸사이클
    interval_R = (n - num) % (2 * w)   # 사이클을 돌고 남은 박스의 수
    result = 1 + 2 * interval_Q # 자기 자신 박스 + 1사이클 박스 2개
    if interval_R >= 2 * (w - 1 - col) + 1:
        result += 1
    return result


# 8이라고 치면 Q = 1 R = 2 result = 3
# 11이면 Q = 0 R = 11