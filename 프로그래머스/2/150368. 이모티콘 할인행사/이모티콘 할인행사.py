from itertools import product
def solution(users, emoticons):
    answer = [0, 0]
    cases = [10, 20, 30, 40]
    for case in product(cases, repeat = len(emoticons)):
        total_price, member = 0, 0
        for rate, price in users:
            pay = 0
            for i, emoticon in enumerate(emoticons):
                if case[i] >= rate:
                    pay += emoticon * (100 - case[i]) // 100
            if pay >= price:
                member += 1
            else:
                total_price += pay
        if member > answer[0]:
            answer[0], answer[1] = member, total_price
        elif member == answer[0] and total_price > answer[1]:
            answer[1] = total_price

    
    return answer


