def solution(today, terms, privacies):  # 모든 달은 28일까지
    answer = []
    n = len(privacies)
    t1, t2 = [], []
    for term in terms:
        key, value = term.split()
        t1.append(key)
        t2.append(value)

    t = dict(zip(t1, t2))

    def to_days(date_str):
        y, m, d = map(int, date_str.split("."))
        return y * 12 * 28 + m * 28 + d

    today_days = to_days(today)

    year, month, day, terms_type = [], [], [], []
    for p in privacies:
        y, m, d = p.split(".")
        year.append(int(y))
        month.append(int(m))
        d, term_type = d.split()
        day.append(int(d))
        terms_type.append(term_type)

    for i in range(n):
        collected_date = f"{year[i]}.{month[i]:02d}.{day[i]:02d}"
        collected_days = to_days(collected_date)
        term_month = int(t[terms_type[i]]) # 약관 유효기간
        expire_days = collected_days + term_month * 28 - 1

        if expire_days < today_days:
            answer.append(i + 1)

    return answer
