from collections import defaultdict

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    
    def to_min(t):  # "HH:MM" -> 분
        h, m = map(int, t.split(":"))
        return h * 60 + m

    in_time = {}              
    total = defaultdict(int)     # 누적 주차 시간

    for rec in records:
        time_str, car, action = rec.split()   # "05:34 5961 IN" -> ("05:34","5961","IN")
        t = to_min(time_str)
        if action == "IN":
            in_time[car] = t
        else:  # OUT
            total[car] += t - in_time.pop(car)

    # 출차 기록 없는 차량
    END = 23 * 60 + 59  # 1439
    for car, t_in in in_time.items():
        total[car] += END - t_in

    def calc_fee(minutes):
        if minutes <= base_time:
            return base_fee
        over = minutes - base_time
        units = (over + unit_time - 1) // unit_time  # 올림
        return base_fee + units * unit_fee

    # 차량번호 오름차순으로 요금 반환
    result = []
    for car in sorted(total.keys()):   # 차량번호 오름차순
        fee = calc_fee(total[car])     # 요금 계산
        result.append(fee)             # 결과 리스트에 추가
    return result
